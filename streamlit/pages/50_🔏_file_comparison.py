import streamlit as st
import difflib
from common.utils import show_line_by_line_comparison, summarize_diffs

with st.form("File comparison"):
    columns = st.columns(2)
    with columns[0]:
        file_A = st.file_uploader("File A")
        if file_A:
            filename_A = file_A.name
    with columns[1]:
        file_B = st.file_uploader("File B")
        if file_B:
            filename_B = file_B.name

    use_default_files = st.checkbox("Use demo files")
    upload_button = st.form_submit_button("実行")

if upload_button or "upload_pressed" in st.session_state :
    st.session_state["upload_pressed"] = True
    if upload_button:
        st.session_state["compare_pressed"] = False
        st.session_state["prepare_pressed"] = False

    valid_files = True
    if use_default_files:
        with open(filename_A := "pages/22_🖼️_image_edit_matched_simple.py") as f :
            contents_A = f.readlines()
        with open(filename_B := "pages/21_🖼️_image_edit_matched.py") as f :
            contents_B = f.readlines()
    elif file_A and file_B:
        contents_A = [s.decode("utf-8") for s in file_A.readlines()]
        contents_B = [s.decode("utf-8") for s in file_B.readlines()]
    else:
        st.error("Please upload both files or use the demo files checkbox")
        valid_files = False
    
    if valid_files:
        diffs = difflib.SequenceMatcher(a=contents_A, b=contents_B)
        st.text(f"The matching percentage of the files is: {diffs.ratio()*100:.2f}%")

        difference_button = st.button("Show full difference")
        if difference_button or (
            "compare_pressed" in st.session_state and st.session_state["compare_pressed"]
            ):
            if difference_button:
                st.session_state["prepare_pressed"] = False
            st.session_state["compare_pressed"] = True 

            show_line_by_line_comparison(st, contents_A, contents_B, False)

            checkboxes = []
            with st.form("Download Delta"):
                cols = st.columns(4)
                for symbol, col in zip(("++", "--", "≠", "=="), cols):
                    with col:
                        checkboxes.append(st.checkbox(symbol, value=True))
                prepare_button = st.form_submit_button("Prepare download")
            
            if prepare_button or ("prepare_pressed" in st.session_state and st.session_state["prepare_pressed"]):
                st.session_state["prepare_pressed"] = True
                content = summarize_diffs(diffs, contents_A, contents_B, *checkboxes)
                st.download_button(
                    label="Download File",
                    key="download_btn",
                    file_name=f"diff-{filename_A}--{filename_B}.txt",
                    data=content)