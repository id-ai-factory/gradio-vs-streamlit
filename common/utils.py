import numpy as np
from loguru import logger
import difflib
import textwrap

def sepia(input_img):
    if input_img is None:
        return input_img
    
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


def summarize_diffs(diffs:difflib.SequenceMatcher, file_A, file_B):
    summary = ["type,line_nr_A,line_nr_B,content_A,content_B"]

    for opcode in diffs.get_grouped_opcodes():
        for diff in opcode:
            logger.debug(f"THe diff is: {diff}")
            summary.append(",".join([str(c) for c in diff]) + f",{file_A[diff[1]:diff[2]]},{file_B[diff[2]:diff[3]]}")

    return "\n".join(summary)

def _tabulate_code(lines):

    wrapper = textwrap.TextWrapper(width=40)

    return '\n'.join( ['\n\t'.join(wrapper.wrap(line)) \
             for line in lines])

def show_line_by_line_comparison(framework,
                                 compare_to_lines:list,
                                 compare_with_lines:list,
                                 show_context : bool = False):
    if framework.__name__ == "streamlit":
        show_line_by_line_comparison_streamlit(framework, compare_to_lines, compare_with_lines, show_context)
    else:
        show_line_by_line_comparison_gradio(framework, compare_to_lines, compare_with_lines, show_context)

def show_line_by_line_comparison_streamlit(st,
                                 compare_to_lines:list,
                                 compare_with_lines:list,
                                 show_context : bool = False):
    """
    コンフィグの違いを表示する

    Parameters
    ----------
    st
        streamlitハンドル
    compare_to_lines : list
        コンフィグ1
    compare_with_lines : list
        コンフィグ2
    show_context : bool, optional
        違いに表示するとき前と後の行も表示するか

    Returns
    -------
    None.

    """
    smatch = difflib.SequenceMatcher(a= compare_to_lines, b= compare_with_lines)

    prev_end = [-1, -1]
    opcodes = list(smatch.get_grouped_opcodes())
    for diffs in opcodes:
        for diff in diffs:
            if show_context or diff[0] !='equal':
                diff_column = st.columns(2)
                if diff[0]=='insert':
                    preface = '++'
                    color='green'
                elif diff[0] == 'delete':
                    preface = '--'
                    color = 'blue'
                elif diff[0] == 'replace':
                    preface = '≠'
                    color = 'red'
                else:
                    preface = ''
                    color = 'black'
    
                for i in range(2):
                    with diff_column[i]:
                        st.markdown('<p style = color:{}>{} {} ~ {}　行目'.format(color, preface, diff[(i+1)*2-1], diff[(i+1)*2]),
                                    unsafe_allow_html=True)
                        prev_end[i] = diff[(i+1)*2]
    
                if diff[0] != 'insert':
                    with diff_column[0]:
                        st.code(_tabulate_code(compare_to_lines[diff[1]:diff[2]]))
                if diff[0] != 'delete':
                    with diff_column[1]:
                        st.code(_tabulate_code(compare_with_lines[diff[3]:diff[4]]))

        if diffs != opcodes[-1]:
            st.markdown("<h5 style='text-align: center; color: black;'>{}</h5>"
                .format('------------'), unsafe_allow_html=True)

def _markdown_column_contents(color, preface, diff, i):
    return '<p style = color:{}>{} {} ~ {}　行目'.format(color, preface, diff[(i+1)*2-1], diff[(i+1)*2])

def show_line_by_line_comparison_gradio(gr,
                                 compare_to_lines:list,
                                 compare_with_lines:list,
                                 show_context : bool = False):
    """
    コンフィグの違いを表示する

    Parameters
    ----------
    st
        streamlitハンドル
    compare_to_lines : list
        コンフィグ1
    compare_with_lines : list
        コンフィグ2
    show_context : bool, optional
        違いに表示するとき前と後の行も表示するか

    Returns
    -------
    None.

    """
    smatch = difflib.SequenceMatcher(a= compare_to_lines, b= compare_with_lines)

    opcodes = list(smatch.get_grouped_opcodes())
    for diffs in opcodes:
        for diff in diffs:
            if show_context or diff[0] !='equal':


                if diff[0]=='insert':
                    preface = '++'
                    color='green'
                elif diff[0] == 'delete':
                    preface = '--'
                    color = 'blue'
                elif diff[0] == 'replace':
                    preface = '≠'
                    color = 'red'
                else:
                    preface = ''
                    color = 'black'
                
                with gr.Row():
                    with gr.Column():
                        gr.Markdown(_markdown_column_contents(color, preface, diff, 0))

                        if diff[0] != 'insert':
                            gr.Code(_tabulate_code(compare_to_lines[diff[1]:diff[2]]))

                    with gr.Column():
                        gr.Markdown(_markdown_column_contents(color, preface, diff, 1))               

                        if diff[0] != 'delete':
                            gr.Code(_tabulate_code(compare_with_lines[diff[3]:diff[4]]))

        if diffs != opcodes[-1]:
            gr.Markdown("<h5 style='text-align: center; color: black;'>{}</h5>"
                .format('------------'))