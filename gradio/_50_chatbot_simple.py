import gradio as gr

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(submit_btn=True, show_label=False)

    def respond(message:str, chat_history:list[dict[str,str]]):
        chat_history.append({"role": "user", "content": message})
        bot_reply = message[::-1]
        chat_history.append({"role": "assistant", "content": bot_reply})
        
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
