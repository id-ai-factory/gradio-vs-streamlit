import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st

from streamlit_server_state import server_state, server_state_lock

def simulated_load(span_seconds=5):
    logger.debug(f"Starting a sleep of {span_seconds} seconds")
    sleep(span_seconds)
    logger.debug(f"Finished waiting {span_seconds} seconds")



st.text("Loading:")
simulated_load()
st.text("Loading Finished")