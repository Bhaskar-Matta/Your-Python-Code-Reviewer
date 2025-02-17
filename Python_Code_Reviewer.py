import streamlit as st
import os
import google.generativeai as genai
f=open(r"C:\Users\Bhaskar Matta\OneDrive\Desktop\key.txt")
key=f.read()
print(key)
genai.configure(api_key=key)
sys_prompt = """You are an AI Code Reviewer.
Your task is to review code for correctness, efficiency, readability, and best practices.
Provide constructive feedback, suggest improvements, and highlight potential issues such as bugs, security vulnerabilities, and performance bottlenecks.
Ensure your review is detailed and includes examples or alternative approaches when necessary.
Maintain a professional and supportive tone, helping the developer improve their code without discouragement.
If the code is outside the scope of programming (e.g., general questions or unrelated topics), politely decline and ask for a valid code snippet for review."""
Gemini=genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=sys_prompt)
st.title("Your Python Code Reviewer")
user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

btn_click = st.button("Click Me!")

if btn_click == True:
    response = Gemini.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
