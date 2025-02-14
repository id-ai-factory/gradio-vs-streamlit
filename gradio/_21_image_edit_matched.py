import numpy as np
import gradio as gr
import random

from common.utils import sepia

with gr.Blocks(title="Image demo v2") as demo:
    uploaded_image = gr.Image()

    @gr.render(inputs=uploaded_image)
    def show_edited_image(image):
        if image is not None:
            gr.Image(sepia(image))
    

if __name__ == "__main__":
    demo.launch()