import gradio as gr

with gr.Blocks() as demo:

    gr.HTML('<iframe src="http://127.0.0.1:6601" title="Streamlit Portal" '+
            'style="height:720px;width:100%;"></iframe>', min_height=720)    

if __name__ == "__main__":
    demo.launch()