import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found!")
    st.stop()

genai.configure(api_key=API_KEY)

# Model
model = genai.GenerativeModel('gemini-1.5-pro-latest')
# UI
st.set_page_config(page_title="ApexGuard AI", layout="centered")

st.title("🛡️ ApexGuard AI")
st.subheader("🚨 Advanced Deepfake Detection System")

uploaded_file = st.file_uploader("📤 Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        st.image(img, caption="📷 Uploaded Image", use_container_width=True)

        prompt = """
        You are an expert AI in deepfake detection.

        Analyze this image carefully for:
        - Face distortion
        - Lighting mismatch
        - Skin texture issues
        - Background inconsistencies

        Output format:
        Deepfake Score: (0-100)
        Reason:
        Verdict: (Real / Suspicious / Fake)
        """

        with st.spinner("🔍 Scanning with AI Engine..."):
            response = model.generate_content([prompt, img])

        result = response.text

        # 🎯 Extract score
        score = 50
        for line in result.split("\n"):
            if "Score" in line:
                try:
                    score = int(''.join(filter(str.isdigit, line)))
                except:
                    pass

        st.success("✅ Analysis Complete")

        # 📊 Score bar
        st.markdown("### 📊 Confidence Score")
        st.progress(score)

        # 🚨 Verdict UI
        if score > 70:
            st.error("🚨 High Risk: Deepfake Detected")
        elif score > 40:
            st.warning("⚠️ Suspicious Image")
        else:
            st.success("✅ Likely Real Image")

        # 🧠 Detailed Output
        st.markdown("### 🧠 AI Analysis")
        st.write(result)

        # 📄 Report download
        report = f"""
        ApexGuard AI Report
        -----------------------
        Score: {score}

        {result}
        """

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="deepfake_report.txt"
        )

    except Exception as e:
        st.error(f"❌ Error: {e}")

st.caption("⚡ Developed by Team The Apex AI")
