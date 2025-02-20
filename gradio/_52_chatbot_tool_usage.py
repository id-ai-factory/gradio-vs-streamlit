import gradio as gr
from common.utils import sepia
from PIL import Image
import numpy as np

def process_file(file_path):
    # Unlike in the image example, the file will be a path and not an image object
    image = Image.open(file_path)
    img_array = np.array(image)[:,:,:3]

    return sepia(img_array)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", height=600)
    # Multimodal allows for appending files. Count and type can be set via parameters
    msg = gr.MultimodalTextbox(submit_btn=True, show_label=False,placeholder="Enter message or upload file")

    def respond(message:dict, chat_history:list[dict[str,str]]):
        # Iterate through files and add them to history.
        # For the use case of this demo we will save the last file
        for file in message["files"]:
            chat_history.append({"role": "user", "content": {"path": (last_file := file)}})
            
        # Add text. I prefer text above, but it was easier to screen caputre this way
        if message["text"] is not None:
            chat_history.append({"role": "user", "content": message["text"]})
            
        # Add the text bit for the assistant
        chat_history.append({"role": "assistant", "content": "Sure thing, here you go"})
        # metadata will be stylized to look like a tool usage
        chat_history.append(
            gr.ChatMessage(
                role="assistant",
                content="Used Filter: Sepia",
                metadata={"title": "🛠️ Used tool: 🖼️ Image Processing"})
        )
        # The content can be most Gradio objects
        chat_history.append({"role":"assistant", "content": gr.Image(process_file(last_file))})

        return "", chat_history

    # The submit is the same as in the simple example; the only difference is the datatype of the msg obj
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
