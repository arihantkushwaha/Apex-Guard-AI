import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup
API_KEY = "AIzaSyC06CgY1WknshJJb-T-bxLfGrCbk7ZpSd4"
# 'transport=rest' गूगल को नए रास्ते से कॉल करने के लिए मजबूर करेगा
genai.configure(api_key=API_KEY, transport='rest')

# Stable Model call
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("Scanning with AI Engine...")
    try:
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)
        
        # Expert Analysis
        response = model.generate_content(["Is this image a deepfake? Give safety score 0-100.", img])
        
        st.success("✅ Analysis Complete!")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

st.caption("Developed by Team The Apex AI")
