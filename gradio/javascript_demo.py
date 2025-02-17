import gradio as gr

head = f"""
<meta name="description" content="Example case of using the head parameter">
<meta name="keywords" content="Gradio Javascript Demo">
<meta name="author" content="ID AI Factory">
"""

resolution_jscript = """
function getResolution() {
    var width = window.screen.width;
    var height = window.screen.height;

    var referenceElement = document.getElementById('window-mkdown-marker');
    if (referenceElement) {
        referenceElement.textContent += width + 'x' + height;
    }
    return width + 'x' + height;
}
"""

with gr.Blocks(head=head, js=resolution_jscript) as demo:
    textbox = gr.Text("Hello")

    resolution_text = gr.Markdown("The Resolution of your screen is: ",elem_id="window-mkdown-marker")

    update_greeting = gr.Button("Update Button")
    update_greeting.click(
        None,
        textbox,
        textbox, 
        js="""(x) => new Promise((resolve) => {
            navigator.geolocation.getCurrentPosition((position) => {
                resolve(x + ', user from ' + `${position.coords.latitude}, ${position.coords.longitude}`);
            });
        })""")

demo.launch()