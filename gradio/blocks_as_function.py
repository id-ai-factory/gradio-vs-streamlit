import gradio as gr

translate = gr.load(name="spaces/gradio/english_translator")

demo = gr.Interface(
    lambda s:translate(s) if s else "",
    inputs=gr.Text(label="Text to Translate",placeholder="Where is the post office?"),
    outputs=gr.Text(label="Translated into German"),
    flagging_mode="never",
    submit_btn="Translate"
)

demo.launch()