import streamlit as st
import time as t
from langchain_ollama.llms import OllamaLLM

#Luigi model
llama_model = OllamaLLM(model="deepseek-r1:1.5b")

# Streamlit front
st.title("Your buddy LUIGI 🤖")
st.write("### Welcome! Ask me a question, and I'll try to help you 😎!")

# Sidebar
st.sidebar.title("AI Helpdesk")
st.sidebar.selectbox("Why you came here?🤔", ["TimePass", "to Study", "to Chill"])
st.sidebar.checkbox("I agree to the terms and conditions")

# Input box for the prompt
prompt = st.text_input("Ask me anything😏:")

if prompt:
    if st.button("Send"):
        with st.spinner("In progress..."):
            t.sleep(3)
        
        st.success("Question submitted successfully!!")
        
        
        funny_prompt = f"Luigi, someone says: '{prompt}'. Respond in the funniest way!"
        chat = llama_model.invoke(funny_prompt)
        st.write("Luigi:", chat)