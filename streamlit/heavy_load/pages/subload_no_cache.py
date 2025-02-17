import streamlit as st
from loguru import logger
from time import sleep
import streamlit as st

from common.utils import simulated_load

st.text("Loading:")
simulated_load()
st.text("Loading Finished")