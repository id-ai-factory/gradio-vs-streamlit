import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st
from streamlit_server_state import server_state, server_state_lock

from common.utils import simulated_load


cols = st.columns(3)

with cols[0]:
    st.text("Loading Server cached")
    with server_state_lock["caching_state_svs"]:  # Lock the "count" state for thread-safety
        if "caching_state_svs" not in server_state:
            simulated_load()
            server_state.caching_state_svs = True

    st.text("Loading Finished")

with cols[1]:

    st.text("Loading Session cached")
    if "caching_demo_ss" not in st.session_state:
        simulated_load()
        st.session_state["caching_demo_ss"] = True
    st.text("Loading Finished")

with cols[2]:
    st.text("Loading No cache")
    simulated_load()
    st.text("Loading Finished")

st.button("Button")