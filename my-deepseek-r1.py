# Author: Emir SELENGİL

import streamlit as st
import requests
import re

st.title('🐋 My Deepseek R1')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("Give me a prompt:")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner('Cevap Oluşturuluyor:'):
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-r1:14b",
                "prompt": prompt,
                "stream": False
            }
        )
        
        answer = res.json()['response']
        
        cleaned_answer = re.sub(r'<think>.*?</think>\s*', '', answer, flags=re.DOTALL)
        
        st.chat_message("ai").write(cleaned_answer)
        st.session_state.messages.append({"role": "ai", "content": cleaned_answer})
