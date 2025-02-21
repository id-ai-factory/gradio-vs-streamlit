import gradio as gr
from common.utils import sepia
import time
from loguru import logger

def artificially_slowed_filter(image):
    logger.info("Starting filter")
    time.sleep(5)
    logger.info("Filter done")
    return sepia(image)


with gr.Blocks() as demo:
    image = gr.Image()
    with gr.Row():
        generate_default = gr.Button("Sepia Default")
        generate_max_1 = gr.Button("Sepia Max 1")
        generate_max_5 = gr.Button("Sepia Max 5")
        generate_unlimited = gr.Button("Sepia No Limit")
    generate_default.click(artificially_slowed_filter, image, image)
    generate_max_1.click(lambda im:artificially_slowed_filter(im), image, image, concurrency_limit=1)
    generate_max_5.click(lambda im:artificially_slowed_filter(im), image, image, concurrency_limit=5)
    generate_unlimited.click(lambda im:artificially_slowed_filter(im), image, image, concurrency_limit=None)

demo.launch()