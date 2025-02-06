import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st

from streamlit_server_state import server_state, server_state_lock

def simulated_load(span_seconds=5):
    logger.debug(f"Starting a sleep of {span_seconds} seconds")
    sleep(span_seconds)
    logger.debug(f"Finished waiting {span_seconds} seconds")

tabs = st.tabs(["First", "Second"])

with tabs[0]:
    st.text("Just Text")

with tabs[1]:
    st.text("Loading:")

    # if "model" not in st.session_state:
    #     simulated_load()
    #     st.session_state["model"] = True
    
    with server_state_lock["count"]:  # Lock the "count" state for thread-safety
        if "model" not in server_state:
            simulated_load()
            server_state.model = True

    st.text("Loading Finished")

st.button("A button")