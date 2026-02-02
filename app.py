import streamlit as st
import google.generativeai as genai

# Setup
st.title("Summary.ai")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Input text
user_input = st.text_area("Paste your long text here:", height=300)

if st.button("Summarize"):
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # The prompt tells the AI how to behave
        response = model.generate_content(f"Summarize this text in 3 bullet points: {user_input}")
        
        st.subheader("Result:")
        st.write(response.text)
    else:
        st.error("Please enter your API Key in the sidebar!")
