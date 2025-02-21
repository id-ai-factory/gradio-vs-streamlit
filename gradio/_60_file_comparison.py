#%%

import gradio as gr
import difflib
from common.utils import show_line_by_line_comparison_gradio, summarize_diffs
import tempfile

#%% 効用関数
def read_file_lines(file_path):
    with open(file_path) as f:
        return f.readlines()

def calculate_difference(use_demo_files, filename_A, filename_B):

    if use_demo_files:
        filename_A = "_22_image_edit_matched_alternative.py"
        filename_B = "_21_image_edit_matched.py"

    elif not (filename_A and filename_B):
        return [gr.Warning("Please upload both files or use the demo files checkbox"), 
                gr.Button(),
                []
        ]
    
    contents_A = read_file_lines(filename_A)
    contents_B = read_file_lines(filename_B)
    diffs = difflib.SequenceMatcher(a=contents_A, b=contents_B)

    return [
        gr.Markdown(f"The matching percentage of the files is: {diffs.ratio()*100:.2f}%", visible=True),
        gr.Button(visible=True),
        [contents_A, contents_B]
    ]

def prepare_download_path(contents, added, removed, replaced, unchanged):
    if not contents:
        return None
    contents_A, contents_B = contents
    
    diffs = difflib.SequenceMatcher(a=contents_A, b=contents_B)
    with tempfile.NamedTemporaryFile(delete=False, prefix="difference_",suffix=".txt") as tmp_file:
        tmp_file.write(summarize_diffs(diffs, contents_A, contents_B, added, removed, replaced, unchanged).encode('utf-8'))

        return tmp_file.name

#%% ページ本体
    
with gr.Blocks(title="File Comparator") as demo:
    file_cache = gr.State([])
    
    gr.Markdown("# Compare Files")
    with gr.Row():

        file_output_A = gr.File(label="File A")
        file_output_B = gr.File(label="File B")

    use_demo_files = gr.Checkbox(label = "Use demo files")
    execute_button = gr.Button("実行")

    comparison_simple_result = gr.Markdown(visible=False)
    show_details_button = gr.Button("Show full difference", visible=False)

    execute_button.click(calculate_difference, 
                         inputs=[use_demo_files, file_output_A, file_output_B], 
                         outputs=[comparison_simple_result, show_details_button, file_cache]) 
    
    # show_details_button.click()
    @gr.render(inputs=file_cache, triggers=[show_details_button.click])
    def show_edited_image(files):
        if len(files)==2:
            fa, fb = files[0], files[1]
            show_line_by_line_comparison_gradio(gr, fa, fb)

        gr.Markdown("---\n### ダウンロード設定")
    
    checkboxes = []
    with gr.Row():
        for symbol in ("++", "--", "≠", "=="):
            checkboxes.append(gr.Checkbox(True, label=symbol, visible=False))
    
    download_button = gr.DownloadButton(value=prepare_download_path, inputs=[file_cache] + checkboxes, visible=False)
    
    show_details_button.click(lambda:[*[gr.Checkbox(visible=True)]*4, gr.DownloadButton(visible=True)],
                              outputs=[*checkboxes, download_button])
    

if __name__ == "__main__":
    demo.launch()