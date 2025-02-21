import time

import streamlit as st
import pandas as pd

from common.utils import sensor_data

if "history" not in st.session_state:
    st.session_state.history = []

current_value = sensor_data()
st.session_state.history.append(current_value)


st.text_input("The Current Value is:",value=current_value, disabled=True)
df = pd.DataFrame({
    "time": range(len(st.session_state.history)),
    "temp": st.session_state.history
    }, 
    
).set_index("time")

st.line_chart(df)

time.sleep(1)
st.rerun()