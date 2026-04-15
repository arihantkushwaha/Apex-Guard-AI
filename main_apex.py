import streamlit as st
from google import genai
from PIL import Image
import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found! Please set GOOGLE_API_KEY in Secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)

st.title("🛡️ ApexGuard AI")

uploaded_file = st.file_uploader("Upload Image", type=['jpg','jpeg','png'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)

    with st.spinner("Analyzing..."):
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=["Check if this is a deepfake image", img]
        )

    st.write(response.text)
