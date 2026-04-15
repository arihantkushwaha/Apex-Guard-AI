import streamlit as st
import google.generativeai as genai

# Setup
genai.configure(api_key="AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🛡️ ApexGuard AI")
st.subheader("Deepfake Detection")

uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("Scanning...")
    try:
        # Simple analysis
        response = model.generate_content(["Is this a deepfake?", uploaded_file.getvalue()])
        st.success("✅ Complete!")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
