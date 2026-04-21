import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Step 1: Configuration ---
# Your New API Key
API_KEY = "AIzaSyDfklMZIOviUu6HR2TVB1EhDBBtMQolwBo"

# transport='rest' ensures we use the most stable connection
genai.configure(api_key=API_KEY, transport='rest')

# Force-loading the stable flash model
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 2: UI Design ---
st.set_page_config(page_title="The Apex AI", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake & AI Fraud Detection")
st.write("Detecting synthetic media using Google Gemini AI.")

# Sidebar for language
language = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi"])

# File Uploader
uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Scanning media... please wait.")
    
    try:
        # Process image with PIL
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_container_width=True)
        
        # Expert Analysis
        if language == "English":
            prompt = "Is this image a deepfake or AI-generated? Give a safety score 0-100 and brief reasons."
        else:
            prompt = "क्या यह इमेज डीपफेक या AI जनरेटेड है? 0-100 के बीच सेफ्टी स्कोर और कारण बताएं।"

        # Generating Content
        response = model.generate_content([prompt, img])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### 📊 Apex Report:")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"System Error: {e}")
        st.info("Please Reboot the app from 'Manage App' settings if error persists.")

st.divider()
st.caption("Developed by Team The Apex AI | Solution Challenge 2026")
