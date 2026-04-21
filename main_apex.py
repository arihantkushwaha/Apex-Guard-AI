import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup
API_KEY = "AIzaSyDfklMZIOviUu6HR2TVB1EhDBBtMQolwBo"
genai.configure(api_key=API_KEY)

# Stable Model path
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection Tool")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("Scanning media...")
    try:
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)
        
        # Expert analysis call
        response = model.generate_content(["Is this a deepfake? Give safety score 0-100", img])
        
        st.success("✅ Analysis Complete!")
        st.write(response.text)
    except Exception as e:
        st.error(f"System Message: {e}")
