import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Step 1: Google Gemini Setup with NEW API KEY ---
API_KEY = "AIzaSyC06CgY1WknshJJb-T-bxLfGrCbk7ZpSd4" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 2: Website UI ---
st.set_page_config(page_title="The Apex AI", page_icon="🛡️")
st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection Shield")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Scanning with Gemini AI Stable Engine...")
    try:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_container_width=True)
        
        # Expert Analysis Call
        response = model.generate_content([
            "Analyze if this image is a deepfake or AI generated. Give a safety score 0-100 and reasons.", 
            img
        ])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### Result:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.caption("Developed by Team The Apex AI | Solution Challenge 2026")
