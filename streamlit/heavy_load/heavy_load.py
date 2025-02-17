import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st
from streamlit_server_state import server_state, server_state_lock

from common.utils import simulated_load

tabs = st.tabs(["First", "Second"])

with tabs[0]:
    st.text("Just Text")

with tabs[1]:
    st.text("Loading:")
    simulated_load()
    st.text("Loading Finished")

st.button("A button")