import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Sales Assistant Prototype")

# Conversation context input with a larger text area
st.subheader("Customer Conversation Context")
user_input = st.text_area("Enter the current conversation context or customer query:", height=150)

# Additional input fields for target company information
st.subheader("Target Company Information")
company_name = st.text_input("Company Name", placeholder="e.g., Acme Corporation")
established_year = st.number_input("Established Year", min_value=1800, max_value=2100, value=2000)
industry = st.text_input("Industry", placeholder="e.g., Technology")
num_employees = st.number_input("Number of Employees", min_value=1, step=1, value=50)

if st.button("Get Sales Response"):
    if user_input:
        # Construct the prompt using both conversation context and company info
        prompt = (
            f"You are a top-performing salesperson. Based on the conversation context: '{user_input}', "
            f"and considering the following target company details:\n"
            f"- Company Name: {company_name}\n"
            f"- Established Year: {established_year}\n"
            f"- Industry: {industry}\n"
            f"- Number of Employees: {num_employees}\n\n"
            "Provide a detailed, model answer that would help overcome objections and steer the conversation effectively."
        )
        try:
            # Query the OpenAI API using the ChatCompletion endpoint
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert sales advisor."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=5000,  # Set to a high value to allow longer responses
                temperature=0.7
            )
            answer = response.choices[0].message['content'].strip()
            st.subheader("Suggested Response:")
            st.write(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some context before clicking 'Get Sales Response'.")
