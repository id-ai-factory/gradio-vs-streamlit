import streamlit as st

st.header("Streamlit Demo")

st.text("左のメニューからデモページを選択してください")
st.markdown("説明省は[このリンク](x)でアクセスできます")

st.markdown('<a href="/simple_text" target="_self">文字列入力</a>から始めましょう！',unsafe_allow_html=True)