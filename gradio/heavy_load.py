import gradio as gr
from common.utils import simulated_load
from loguru import logger
import random

def unconditional():
    simulated_load()
    return "Finished loading (always)"

def check_session_first(ss):
    if "model" not in ss:
        simulated_load()
        ss["model"] = True
    return "Finished Loading (per session)"

def check_server_first(ss):
    if not ss:
        simulated_load()

    return "Finished loading (per restart)"

with gr.Blocks() as demo:
    state = gr.State({})

    with gr.Tab("First"):
        gr.Markdown("Simple Page")
    
    with gr.Tab("Second"):
        gr.Markdown("Loading (when the server starts)")
        simulated_load()
        server_model = True
        gr.Markdown("Loaded")
    gr.Markdown("Just text")

    status_text = gr.Label("Not loading")
    with gr.Row():
        every = gr.Button("On every click")
        per_session = gr.Button("Once per session")
        per_restart = gr.Button("On Startup")

        every.click(unconditional, outputs=status_text)
        per_session.click(check_session_first, inputs=state, outputs=status_text)
        per_restart.click(lambda: check_server_first(server_model), outputs=status_text)

    # @gr.render()
    # def conditional_load_block():
    #     simulated_load()

demo.launch()