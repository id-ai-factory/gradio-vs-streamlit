import streamlit.components.v1 as components

# 動的にURLを取りたい場合は以下を使ってください
# pip install streamlit_js_eval は必要です

# from streamlit_js_eval import get_page_location

# page_loc = get_page_location()
# st_url = page_loc["origin"]
# st_url = st_url[:-4] + "6602"


components.iframe("http://127.0.0.1:6602", height=720, scrolling=True)
