import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st

from common.utils import simulated_load

key = "subload_ss_finished"

st.text("Loading:")

if key not in st.session_state:
    simulated_load()
    st.session_state[key] = True

st.text("Loading Finished")
