import numpy as np
import gradio as gr
import random

from common.utils import sepia

with gr.Blocks(title="Image Demo v3") as demo:
    uploaded_image = gr.Image()
    processed_image = gr.Image(visible=False)

    uploaded_image.change(
        lambda image: gr.Image(sepia(image), visible=True), 
        inputs=[uploaded_image], 
        outputs=[processed_image]
    )
    

if __name__ == "__main__":
    demo.launch()