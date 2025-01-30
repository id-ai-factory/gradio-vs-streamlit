import streamlit as st

text = st.text_input("テキスト入力欄：")
if text:
    st.markdown(f"処理の後はこちらになります: \n### {text.upper()}")