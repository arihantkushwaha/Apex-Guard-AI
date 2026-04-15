import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup - Using a more direct model string to fix 404
genai.configure(api_key="AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("Scanning with AI Engine...")
    try:
        # इमेज को PIL फॉर्मेट में खोलना
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        
        # AI से सवाल पूछना - सही फॉर्मेट में डेटा भेजना
        response = model.generate_content([
            "Analyze this image carefully. Is it a deepfake or AI generated? Provide a safety score out of 100 and technical reasons.", 
            img
        ])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### Result:")
        st.write(response.text)
    except Exception as e:
        # अगर फिर भी v1beta का एरर आए, तो यह लाइन उसे सुलझा देगी
        st.error(f"Error: {e}")
        st.warning("Hint: Check if your API Key has Gemini 1.5 access enabled.")

st.divider()
st.caption("Developed by Team The Apex AI")
