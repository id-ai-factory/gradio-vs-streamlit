import gradio as gr

iframe_js = """
function createLocalhostIframe() {
    var iframe = document.createElement('iframe');
    iframe.id = 'streamlit-portal-iframe';
    iframe.style.width = '100%';
    iframe.style.height = '720px';
    iframe.style.border = 'none';

    var currentUrl = new URL(window.location.href);
    currentUrl.port = '6601'; 
    currentUrl.pathname = ''; // In the portal this would add /streamlit-portal
    currentUrl.search = ''; // ditto
    currentUrl.hash = ''; // ditto
    iframe.src = currentUrl.toString(); 


    var referenceElement = document.getElementById('the-iframe-goes-under-this');

    // Insert the iframe directly after the reference element
    if (referenceElement) {
        referenceElement.parentNode.insertBefore(iframe, referenceElement.nextSibling);
        return 'Iframe added';
    }
    return "Failed to add element -- target ID missing";
    
}
"""

def add_iframe_block(title="Streamlit Portal Dynamic"):
    gr.Markdown("",visible=False, elem_id="the-iframe-goes-under-this")
    

if __name__ == "__main__":
    with gr.Blocks(js=iframe_js) as demo:
        add_iframe_block()
    demo.launch()
