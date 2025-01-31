import gradio as gr
import pandas as pd

df = pd.read_csv('common/user_data.csv')
df['date_registered'] = pd.to_datetime(df['date_registered'])

styler = df.style.hide(subset=["credits_used"], axis=1)\
    .relabel_index(["username","email","日付","available_credits","active"], axis=1)

with gr.Blocks() as demo:
    gr.DataFrame(
        styler, 
        datatype=["str", "str", "date", "number", "number", "bool"],
        interactive=False,
    )

demo.launch()