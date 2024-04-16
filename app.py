from openai import OpenAI
import streamlit as st

# Read the API key from a file
with open("key/api_key.txt") as f:
    key = f.read().strip()

# Setup an OpenAI Client
client = OpenAI(api_key=key)

# Streamlit UI
st.snow()
st.title('AI Code Reviewer')
st.subheader("Enter your Python code")

# Prompt
prompt = st.text_area("Enter your code: ")

# OpenAI Code
if st.button('Generate'):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "Welcome, AI Debugger! Your role is to assist users by identifying and fixing bugs in Python code. Your output should be a clear explanation of the detected bugs and the corrected code."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
        st.balloons()
    except Exception as e:
        st.error(f"An error occurred: {e}")
