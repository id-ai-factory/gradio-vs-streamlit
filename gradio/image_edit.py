import numpy as np
import gradio as gr

from common.utils import sepia

with gr.Blocks() as demo:
    gr.Interface(sepia, "image", "image", flagging_mode="never")
    
    # カメラのみにしたい場合は：
    # gr.Interface(sepia, gr.Image(sources="webcam"), "image", flagging_mode="never")
     
demo.launch()