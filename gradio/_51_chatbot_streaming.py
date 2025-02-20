import gradio as gr
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages",)
    msg = gr.Textbox(submit_btn=True, show_label=False)
    next_message = gr.State([""])

    def bot_reply(history, message_buffer):
        for character in message_buffer[0]:
            history[-1]['content'] += character
            time.sleep(0.05)
            yield history

    def add_user_message(message:str, chat_history:list[dict[str,str]], message_buffer):
        chat_history.append({"role": "user", "content": message})
        message_buffer[0] = message[::-1]
        chat_history.append({"role": "assistant", "content": ""})
        
        return "", chat_history

    msg.submit(add_user_message, [msg, chatbot, next_message],[msg, chatbot], queue=False)\
            .then(bot_reply, [chatbot,next_message], chatbot)
    
demo.launch()
