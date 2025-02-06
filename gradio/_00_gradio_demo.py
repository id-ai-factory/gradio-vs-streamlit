import gradio as gr


# A simpler demonstration
# with gr.Blocks() as demo:
#     gr.Textbox()

# with demo.route("Second Page", "/second"):
#     gr.Number()


with gr.Blocks() as demo:
    gr.Markdown("# Streamlit Demo")

    gr.Markdown("左のメニューからデモページを選択してください")
    gr.Markdown("説明省は[このリンク](x)でアクセスできます")

    gr.Markdown('<a href="/simple_text" target="_self">文字列入力</a>から始めましょう！')

with demo.route("文字列入出力", "/simple_text"):
    import _10_simple_text

with demo.route("画像編集", "/image_edit"):
    import _20_image_edit

with demo.route("画像編集（合わせ）", "/image_edit_matched"):
    import _21_image_edit_matched

with demo.route("画像編集（合わせ）２", "/image_edit_matched_a"):
    import _22_image_edit_matched_alternative

with demo.route("行列、確認版", "/data_manipulator_show"):
    import _31_data_manipulator_show

with demo.route("行列、編集版", "/data_manipulator_edit"):
    import _32_data_manipulation_edit

with demo.route("グラフ", "/chart"):
    import _40_charts

with demo.route("ファイル比較", "/file_comparison"):
    import _50_file_comparison

# v5.15で、マルチページでCheckboxGroupがエラーを起こします
# with demo.route("ファイル比較、代替v", "/file_comparison_alternative"):
#     import _51_file_comparison_alternative

with demo.route("テーマお試し", "/theme_change"):
    import _60_theme_change
    

demo.launch()