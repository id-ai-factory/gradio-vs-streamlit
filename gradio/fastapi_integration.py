from fastapi import FastAPI, responses
import gradio as gr

CUSTOM_PATH = "/gradio"

app = FastAPI()

@app.get("/", response_class=responses.HTMLResponse)
def read_main():
    return 'Greetings from the FastAPI APP.<p><a href=/gradio>Go to Gradio</a></p>'

io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
