import gradio as gr
import pandas as pd
from common.utils import sensor_data

with gr.Blocks() as demo:
    data_val = gr.Textbox(sensor_data, label="The current value is: ", interactive=False, every=1)

    history = gr.State([])

    plot = gr.LinePlot(
        x = "time",
        y = "temp",
        label="Value History",
        y_lim=[10,30]
        )
    
    data_val.change(lambda val, hist: (
            (new_hist:=hist + [float(val if val else 20.0)]),
            pd.DataFrame({
                "time": range(len(new_hist)),
                "temp" : new_hist,
                })),
            inputs=[data_val, history], 
            outputs=[history, plot])

demo.launch()
