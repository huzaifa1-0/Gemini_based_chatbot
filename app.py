import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Google Generative AI Streamlit App",
    page_icon=":robot:",
    layout="centered",
)

Google_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=Google_API_KEY)

# Initialize the model correctly
model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model initialization

def map_role(role):
    return "assistant" if role == "model" else "user"  # Fixed role mapping

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Google Generative AI Streamlit App")
st.write("This is a simple Streamlit app that uses Google Generative AI to generate text.")

for message in st.session_state.chat_session.history:
    with st.chat_message(map_role(message.role)):
        st.markdown(message.parts[0].text)

user_input = st.chat_input("Type your message here...")

if user_input:
    # Corrected line without is_user parameter
    st.chat_message("user").markdown(user_input)
    response = st.session_state.chat_session.send_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response.text)