import gradio as gr
import pandas as pd
from loguru import logger

df = pd.read_csv('common/user_data.csv')
df['date_registered'] = pd.to_datetime(df['date_registered'])


def print_results(df):
    logger.info(f"Jdoe updated to: {df.loc[df["username"]=="jdoe"]}")

with gr.Blocks() as demo:
    data_frame_interactive = gr.DataFrame(
        df, 
        interactive=True,
    )
    data_frame_interactive.change(
        print_results, 
        inputs=[data_frame_interactive]
    )
    

demo.launch()