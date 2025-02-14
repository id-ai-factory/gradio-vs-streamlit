import numpy as np
import gradio as gr

from common.utils import code_example, sepia

## Locally Available Theme
# theme = "soft"

## Theme published on HuggingFace
# theme = gr.Theme.from_hub("gradio/seafoam")

## Theme Customized using gr.themes.builder()
theme = gr.themes.Monochrome(
    primary_hue=gr.themes.Color(c100="#f4f4f5", c200="#e4e4e7", c300="rgba(190.9871710526316, 190.9871710526316, 213.45625, 1)", c400="rgba(168.4295504385965, 168.4295504385965, 204.265625, 1)", c50="#fafafa", c500="rgba(122.44473684210526, 122.44473684210526, 205.27499999999998, 1)", c600="rgba(123.86641310307017, 123.86641310307017, 203.1765625, 1)", c700="rgba(80.65936129385963, 80.65936129385963, 154.54062499999998, 1)", c800="rgba(73.99683388157895, 73.99683388157895, 165.4046875, 1)", c900="rgba(69.15989583333332, 69.15989583333332, 147.36875, 1)", c950="rgba(17.13560855263158, 17.13560855263158, 139.53281249999998, 1)"),
    secondary_hue="slate",
    text_size="lg",
    spacing_size="sm",
    font=['Courier New', 'ui-sans-serif', 'system-ui', 'sans-serif'],
).set(
    background_fill_primary='*primary_50',
    button_primary_background_fill='*primary_950',
    shadow_drop='*shadow_inset'
)


with gr.Blocks(theme) as demo:
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