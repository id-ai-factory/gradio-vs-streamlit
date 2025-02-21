import gradio as gr

from _71_streamlit_portal_dynamic_url import iframe_js, add_iframe_block
# The import above is a special case if running special JS is needed

# A simpler demonstration
# with gr.Blocks() as demo:
#     gr.Textbox()

# with demo.route("Second Page", "/second"):
#     gr.Number()


with gr.Blocks(js = iframe_js, title="Gradio Multi Page Application") as demo: #The HS is necessary for the dynamic URL
    gr.Markdown("# Gradio Demo")

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
    import _30_data_manipulation_show

with demo.route("行列、編集版", "/data_manipulator_edit"):
    import _31_data_manipulation_edit

with demo.route("グラフ", "/chart"):
    import _40_charts

with demo.route("チャットボット（シンプル）", "/chatbot_simple"):
    import _50_chatbot_simple

with demo.route("チャットボット（ストリーム）", "/chatbot_streaming"):
    import _51_chatbot_streaming

with demo.route("チャットボット（ツール）", "/chatbot_tool_usage"):
    import _52_chatbot_tool_usage

with demo.route("チャットボット（本物）", "/chatbot_real"):
    import _53_chatbot_actual


with demo.route("ファイル比較", "/file_comparison"):
    import _60_file_comparison

# v5.15で、マルチページでCheckboxGroupがエラーを起こします
# with demo.route("ファイル比較、代替v", "/file_comparison_alternative"):
#     import _61_file_comparison_alternative

with demo.route("Streamlitポータル（固定）", "/streamlit_portal"):
    import _70_streamlit_portal

    
with demo.route("Streamlitポータル（動的）", "/streamlit_portal_dynamic"):
    add_iframe_block()
    

demo.launch()