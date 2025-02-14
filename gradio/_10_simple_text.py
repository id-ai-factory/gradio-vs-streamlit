import gradio as gr

def validate_input_single(text):
    if text:
        return gr.Markdown(f"出力は{text.upper()}" if text else "",visible=True)
    else:
        return gr.Markdown(visible=False)

def validate_input_multiple(text):
    if text:
        return [
            gr.Label(f"出力は{text.upper()}" if text else "",visible=True),
            gr.Markdown(visible=True)
        ]
    else:
        return [
            gr.Label(visible=False),
            gr.Markdown(visible=False)
        ]

with gr.Blocks(title="Text Demo") as demo:
    

    text_input = gr.Text(label="テキスト入力欄：")
    text_output = gr.Markdown()

    text_input.change(lambda text:f"処理の後はこちらになります: \n### {text.upper()}", 
                       inputs=[text_input],
                       outputs=[text_output])
    
    gr.Markdown("---")

    text_input = gr.Text(label="テキスト入力欄：")
    gr.Markdown(
            lambda text:f"処理の後はこちらになります: \n### {text.upper()}" if text else "",
            inputs=text_input
    )
    # gr.Label(lambda text:f"処理の後はこちらになります: {text.upper()}" if text else "",
    #         inputs=text_input)
    gr.Markdown("---")


    text_input = gr.Text(label="入力欄その３：")
    @gr.render(inputs=text_input)
    def display_result(raw_input):
        if raw_input:
            gr.Markdown(f"必ず処理されたものです: \n### {raw_input.upper()}")

    gr.Markdown("---")

    text_input = gr.Text(label="入力欄その４：")
    mk1 = gr.Label(validate_input_single, inputs=text_input, visible=False)
    gr.Markdown("---")
    
    text_input = gr.Text(label="入力欄その５：")
    mk1 = gr.Label(visible=False)
    mk2 = gr.Markdown("↑↑↑", visible=False)
    text_input.change(validate_input_multiple, inputs=[text_input], outputs=[mk1, mk2])
    
    gr.Markdown("---")

    gr.Interface(
        lambda text1, text2:f"結果: \n### {text1.upper() + text2.upper()}",
        ["text", "text"],
        "markdown",
        flagging_mode="never")
    
if __name__ == "__main__":
    demo.launch()