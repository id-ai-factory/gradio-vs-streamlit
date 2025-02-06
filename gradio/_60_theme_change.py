import numpy as np
import gradio as gr

from common.utils import code_example, sepia

with gr.Blocks() as demo:
    gr.Interface(sepia, "image", "image", flagging_mode="never")
    
    with gr.Tab("Left"):
        gr.Textbox(placeholder="ここに短いテキストを入れてください")
    with gr.Tab("Right"):
        gr.Number()
            
    with gr.Row():
        for symbol in ("A", "B", "C", "D"):
            gr.Checkbox(ord(symbol)%2, label=symbol)
    
    with gr.Row():
        with gr.Accordion("Long text place"):
            gr.TextArea("ここは長い文章も可能です。\nすでに入れているテキストの例です",interactive=True)
        gr.Code(value=code_example(),language="python")

    gr.DownloadButton() 


if __name__ == "__main__":
    demo.launch()