import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Step 1: Configuration ---
# Tumhari New API Key
API_KEY = "AIzaSyC06CgY1WknshJJb-T-bxLfGrCbk7ZpSd4" 

# 'transport=rest' jodne se purana 404 error khatam ho jayega
genai.configure(api_key=API_KEY, transport='rest')

# Stable model ka upyog
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 2: UI Design ---
st.set_page_config(page_title="The Apex AI", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake & AI Fraud Detection")
st.write("Google Gemini AI ki madad se digital fraud se suraksha.")

# Sidebar for language
language = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi"])

# File Uploader
uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Image scan ho rahi hai... Kripya pratiksha karein.")
    
    try:
        # Image ko open karna (Pillow library se)
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_container_width=True)
        
        # Expert Prompts
        if language == "English":
            prompt = "Analyze if this image is a deepfake or AI generated. Look for unnatural textures. Give a safety score (0-100) and reasons."
        else:
            prompt = "Jaanch karein ki kya ye image deepfake ya AI generated hai. 0-100 ke beech safety score dein aur karan batayein."

        # AI Analysis Call
        response = model.generate_content([prompt, img])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### 📊 Apex Report:")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Tip: Agar abhi bhi error aaye, to Streamlit settings se 'Reboot App' karein.")

st.divider()
st.caption("Developed by Team The Apex AI | Solution Challenge 2026")
