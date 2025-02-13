import gradio as gr


def process_text(request: gr.Request, text):
    return f"{request.username} ({request.session_hash}): 処理の後はこちらになります: \n### {text.upper()}"

with gr.Blocks() as demo:
    text_input = gr.Text(label="テキスト入力欄：")
    text_output = gr.Markdown()

    text_input.change(process_text, 
                       inputs=[text_input],
                       outputs=[text_output])
    
    logout_button = gr.Button("Logout", link="/logout")

def same_auth(username, password):
    return username == password

demo.launch(auth=same_auth, auth_message="Please provide a username and password")

# Even more basic auth
# demo.launch(auth=("admin", "pass1234"))