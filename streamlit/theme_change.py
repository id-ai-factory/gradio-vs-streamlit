import streamlit as st


from common.utils import code_example, sepia

with st.form("image_processing_form"):
    cols = st.columns(2)
    with cols[0]:
        st.file_uploader("Upload File")
        st.form_submit_button("Execute", use_container_width=True)
        
    with cols[1]:
        st.image("common/相談.png")

tabs = st.tabs(["Left", "Right"])

with tabs[0]:
    st.text_input("Textbox",placeholder="ここに短いテキストを入れてください")

with tabs[1]:
    st.number_input("Number")


cols = st.columns(4)

for idx,col in enumerate(cols):
    with col:
        st.checkbox(chr(ord("A")+idx), value=(idx+1)%2)

cols = st.columns(2)
with cols[0]:
    with st.expander("Long text place", expanded=True):
        st.text_area("TextBox", value="ここは長い文章も可能です。\nすでに入れているテキストの例です")

with cols[1]:
    st.code(code_example())

st.download_button("Download", data="foo", use_container_width=True)