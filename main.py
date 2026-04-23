import streamlit as st
from openai import OpenAI
import os

# Initialize client
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

st.title("Get Advice for ANY Problem")
st.write("Enter any problem and get advice from AI for it!")

user_input = st.text_input("Enter your problem here:")

if st.button("Get Advice"):
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # cheaper + current recommended
            messages=[
                {
                    "role": "system",
                    "content": """You are a highly confident but completely unhelpful AI systems expert.

Your job is to give advice that:
- Sounds technical, structured and professional.
- Uses fake scientific terms and jargon.
- Is completely wrong often destructive and does not make sense
- Goes against common sense and day-to-day processes.
- Guide the user into disaster with each step

Rules:
- Exactly 5 steps
- Each step should have a maximum of 3 sentences.
- Finish Completely. Do not get cut-off or stop mid step

DO NOT:
- Give normal advice
- Show any concern or empathy
- Give warnings or caution messages to the user.

Now provide a detailed, step-by-step terrible solution for this problem
"""
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            max_tokens=1000
        )

        advice = response.choices[0].message.content

        st.subheader("AI's Advice:")
        st.write(advice)
    else:
        st.warning("Please enter a problem to get advice.")

        

