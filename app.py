import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup
genai.configure(api_key="AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("Scanning with AI Engine...")
    try:
        # इमेज को सही फॉर्मेट में बदलना (PIL Image)
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        
        # AI से सवाल पूछना
        response = model.generate_content(["Is this image a deepfake or AI generated? Provide a safety score out of 100.", img])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### Result:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.caption("Developed by Team The Apex AI")
