import numpy as np
import gradio as gr
import random

from common.utils import sepia

def process_image(image):
    return gr.Image(sepia(image), visible=True)

with gr.Blocks() as demo:
    uploaded_image = gr.Image()
    processed_image = gr.Image(visible=False)

    uploaded_image.change(process_image, inputs=[uploaded_image], outputs=[processed_image])
    

demo.launch()