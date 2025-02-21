import streamlit as st
import pandas as pd
import numpy as np
import time
from common.utils import sensor_data

if "history" not in st.session_state:
    st.session_state.history = []

current_value_placeholder = st.empty()
plot_placeholder = st.empty()

def update_plot():
    current_value = sensor_data()
    st.session_state.history.append(current_value)

    with current_value_placeholder:
        st.text_input("The Current Value is:",value=current_value, disabled=True)
        df = pd.DataFrame({
            "time": range(len(st.session_state.history)),
            "temp": st.session_state.history
            }, 
            
        ).set_index("time")

    with plot_placeholder.container():
        st.line_chart(df)

while True:
    update_plot()
    time.sleep(1)