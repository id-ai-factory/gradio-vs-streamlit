import gradio as gr

with gr.Blocks() as demo:
    
    text_input = gr.Text(label="テキスト入力欄：")
    text_output = gr.Markdown()

    text_input.change(lambda text:f"処理の後はこちらになります: \n### {text.upper()}", 
                       inputs=[text_input],
                       outputs=[text_output])
    
    gr.Markdown("---")

    text_input = gr.Text(label="入力欄その２：")
    @gr.render(inputs=text_input)
    def display_result(raw_input):
        if raw_input:
            gr.Markdown(f"必ず処理されたものです: \n### {raw_input.upper()}")

    gr.Markdown("---")

    gr.Interface(
        lambda text:f"コードの一行で達成したもの: \n### {text.upper()}",
        "text",
        "markdown",
        flagging_mode="never")
demo.launch()