import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Step 1: Configuration ---
# Your New Working API Key
API_KEY = "AIzaSyC06CgY1WknshJJb-T-bxLfGrCbk7ZpSd4" 

genai.configure(api_key=API_KEY)

# Using the most stable model version to avoid 404 errors
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 2: UI Design ---
st.set_page_config(page_title="The Apex AI", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake & AI Fraud Detection")
st.write("Protecting your digital identity with Google Gemini AI.")

# Sidebar for language
language = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi"])

# File Uploader
uploaded_file = st.file_uploader("Upload an Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Analyzing image... Please wait.")
    
    try:
        # Open the image using PIL
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_container_width=True)
        
        # Expert Prompts
        if language == "English":
            prompt = "Analyze if this image is a deepfake or AI generated. Look for unnatural edges and textures. Give a safety score (0-100) and provide a brief reason."
        else:
            prompt = "विश्लेषण करें कि क्या यह इमेज डीपफेक या AI जनरेटेड है। चेहरे की बनावट की जांच करें। 0-100 के बीच सेफ्टी स्कोर दें और कारण बताएं।"

        # AI Analysis Call
        response = model.generate_content([prompt, img])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### 📊 Apex Report:")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        st.info("Tip: If you see a 404 error, please Reboot the app from Streamlit settings.")

st.divider()
st.caption("Developed by Team The Apex AI | Solution Challenge 2026")
