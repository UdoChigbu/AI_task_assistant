
import streamlit as st
import openai
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("API_KEY"))


st.set_page_config(page_title="AI Task Assistant", layout="centered")

st.title("🤖 AI Task Assistant")
st.write("Type in a task or request, and I'll help you manage it!")

task = st.text_input("📝 Your task", placeholder="e.g. Remind me to study discrete math on Tuesday")

if st.button("Get Help") and task:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant for managing tasks."},
                    {"role": "user", "content": task}
                ]
            )
            result = response.choices[0].message.content.strip()
            st.success("Here's what I suggest:")
            st.markdown(f"> {result}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
