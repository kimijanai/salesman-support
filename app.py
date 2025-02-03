import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Sales Assistant Prototype")

# Input field for conversation context or customer query
user_input = st.text_input("Enter the current conversation context or customer query:")

if st.button("Get Sales Response"):
    if user_input:
        # Construct the prompt for the OpenAI API
        prompt = (
            f"You are a top-performing salesperson. Based on the conversation context: '{user_input}', "
            f"provide a model answer that would help overcome objections and steer the conversation effectively."
        )
        try:
            # Query the OpenAI API (using the ChatCompletion endpoint as an example)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert sales advisor."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            answer = response.choices[0].message['content'].strip()
            st.subheader("Suggested Response:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some context before clicking 'Get Sales Response'.")
