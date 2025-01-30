import numpy as np
import gradio as gr
import random

from utils.utils import sepia

with gr.Blocks() as demo:
    uploaded_image = gr.Image()

    @gr.render(inputs=uploaded_image)
    def show_edited_image(image):
        if image is not None:
            gr.Image(sepia(image))
    

demo.launch()