import streamlit as st
import google.generativeai as genai

st.title("🤖 အောင် (Aung) - ကိုယ်ပိုင် AI")
api_key = st.sidebar.text_input("Gemini API Key ကို ထည့်ပါ", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    user_input = st.text_input("ဘာမေးမလဲ?")
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
