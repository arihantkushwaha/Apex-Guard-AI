import streamlit as st
import google.generativeai as genai

# --- Step 1: Google Gemini Setup ---
GOOGLE_API_KEY = "AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk" 

# Model configuration with stable version
genai.configure(api_key=GOOGLE_API_KEY)

# Using the stable model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# --- Step 2: Website UI ---
st.set_page_config(page_title="The Apex AI - Deepfake Guard", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Detecting Deepfakes & Digital Fraud in Real-Time")

language = st.sidebar.selectbox("Language / भाषा", ["English", "Hindi"])

uploaded_file = st.file_uploader("Upload Image/Video/Audio", type=['mp4', 'mov', 'wav', 'mp3', 'jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Scanning with Gemini AI Stable Engine...")
    
    try:
        prompt = "Is this media a deepfake or AI fraud? Give safety score 0-100."
        if language == "Hindi":
            prompt = "क्या यह मीडिया डीपफेक या AI फ्रॉड है? 0-100 के बीच सेफ्टी स्कोर दें।"

        # Correct data format for stable API
        response = model.generate_content([
            prompt,
            {"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}
        ])
        
        st.success("✅ Analysis Complete!")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Try again: {e}")

st.caption("Developed by Team The Apex AI")
