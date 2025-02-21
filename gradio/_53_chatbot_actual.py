#%% Imports
import gradio as gr
from pathlib import Path
import base64
from openai import OpenAI

#%% Utility functions
def encode_image(image_path):
    """ Encode image to base64 (for OpenAI)"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def clear_metadata_and_options(l):
    """ 
    Clear the Gradio specific notation (causes issues in image recognition)
    Also replace file paths with a placeholder
    """
    nl = []
    for i in l:
        nl.append({k: (v if not isinstance(v, tuple) else "<contents of a file>") for k, v in i.items() if k in ["role", "content"] })
    return nl

def analyze_image(history, prompt: str, image_path: str, extension: str):
    """Send an image to the OpenAI API"""

    # First remove tags that can cause a 500 error
    history = clear_metadata_and_options(history)

    # read and encode the image
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= [ 
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/{extension};base64,{base64_image}"}
                }
            ]}
        ],
        temperature=0.5,
        stream=True,
    )
    # If needed for testing, the commented out section can be used with stream=False
    return response 
    # return response.choices[0].message.content

def send_message(chat_history:list[dict[str,str]], rag = ""):
    """ Sends a normal text message to the OpenAI API. If <rag> is provided, it will be added as context"""

    # While the tags won't cause issues, the file paths should be removed
    chat_history = clear_metadata_and_options(chat_history)

    # If context is provided, it is inserted into the last message with a header text
    if rag:
        chat_history = chat_history[:-1]
        chat_history[-1]["content"] += "\n\nContext/additional information:\n" + rag
    
    # send modified history to the API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        stream=True,
    )

    # If needed for testing, the commented out section can be used with stream=False
    return completion 
    # return completion.choices[0].message.content

def complete_token(history, message_buffer):
    """ Yields the reply token by token """
    for chunk in message_buffer:
        character  = chunk.choices[0].delta.content if chunk.choices else ""
        history[-1]['content'] += character or ""
        yield history

#%% Initialization

# Don't forget to remove the API key if you commit the code or a modified version of it to your own repo
client = OpenAI(api_key="<not set>")
# Alternatively use an environmental variable
# import os
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<not set>"))

#%% GUI code
with gr.Blocks() as demo:
    # 800 should be a suitable height for HD
    chatbot = gr.Chatbot(type="messages", height=800)
    # We want the default send arrow (submit_btn) without an unnecessary label on top (show_label)
    # We will add a pretty standard placeholder
    # Multiple files is not allowed
    # The filetypes will be restricted to image, most formats should be ok, + csv and txt
    msg = gr.MultimodalTextbox(submit_btn=True, show_label=False,placeholder="Enter message or upload file",
                               file_count="single", file_types=["image", ".csv", ".txt"])
    
    # We need somewhere to store the generator for the token chunks
    chunks = gr.State(None)

    def respond(message:dict, chat_history:list[dict[str,str]], response):
        """ Initiates the response"""

        # If the user has added test, it is added to the history
        if (prompt:=message["text"]) is not None:
            chat_history.append({"role": "user", "content": prompt})

        # Depending on the file type, we will either read the file or use the path
        extra_context = ""
        for file_path in message["files"]:
            chat_history.append({"role": "user", "content": {"path": (file_path)}})
            if Path(file_path).suffix in [".csv", ".txt"]:
                with open(file_path, "r") as f:
                    extra_context = f.read()
            else:
                extra_context = {"image": file_path}        
        
        # If the context is a dictionary, it is an image, otherwise it is text
        # In both cases the assistant response is initialized to emptystring
        if isinstance(extra_context, dict):
            response = analyze_image(chat_history, prompt, file_path, Path(file_path).suffix[1:])
            chat_history.append({"role": "assistant", "content": ""})
        else:
            response = send_message(chat_history, extra_context)
            chat_history.append({"role":"assistant", "content": ""})

        # We set the user input to emptystring and disable new input
        return gr.MultimodalTextbox("",interactive=False), chat_history, response

    # The submission is treated in 3 parts:
    # 1. Send the request, disable the input field, store the generator for the tokens,
    #    save the user input and initialize the bot history
    # 2. Add the tokens one by one to the chat history (and the display) from the 
    #    generator in the State object
    # 3. Re-enable the input field
    msg.submit(respond, [msg, chatbot], [msg, chatbot, chunks], queue=False).\
        then(complete_token, [chatbot, chunks], chatbot).\
            then(lambda:gr.MultimodalTextbox(interactive=True), outputs=msg)

demo.launch()
