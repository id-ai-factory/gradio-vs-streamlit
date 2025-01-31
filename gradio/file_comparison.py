import gradio as gr
import pandas as pd
from loguru import logger

def upload_file(file):
    return file.name

with gr.Blocks(title="File Comparator") as demo:
    gr.Markdown("# Compare Files")
    with gr.Row():
        # Streamlitのフォーマットを真似したい場合は：
        # with gr.Column():
        #     gr.Markdown("### File A")
        #     gr.UploadButton("Upload")
        with gr.Column():
            file_output = gr.File()
            upload_button_A = gr.UploadButton("Upload File A")
            upload_button_A.upload(upload_file, upload_button_A, file_output)

        with gr.Column():
            file_output = gr.File()
            upload_button_B = gr.UploadButton("Upload File B")
            upload_button_B.upload(upload_file, upload_button_B, file_output)

        

    # gr.Label(lambda file:)

demo.launch()