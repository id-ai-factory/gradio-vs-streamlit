import streamlit as st
import numpy as np


#%% デモ１
# with st.chat_message("👾"):
#     st.write("Greetings Human")

# with st.chat_message("user"):
#     st.write("Hello 👋")
#     st.line_chart(np.random.randn(30, 3))

#%% デモ２
# messages = st.container(height=400)
# if prompt := st.chat_input("Say something"):
#     messages.chat_message("user").write(prompt)
#     messages.chat_message("👾").write(f"Let me reverse that: {prompt[::-1]}")


#%% デモ３
msg_key = "messages" 
if msg_key not in st.session_state:
    st.session_state[msg_key] = []

messages = st.container(height=400)
if prompt := st.chat_input("Say something"):
    st.session_state[msg_key].append(("user", prompt))

    bot_reply = prompt[::-1]
    st.session_state[msg_key].append(("👾", bot_reply))

    for party, message in st.session_state[msg_key]:    
        messages.chat_message(party).write(message)
    