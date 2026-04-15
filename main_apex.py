import streamlit as st
from google import genai
from PIL import Image
import os

# 🔐 API KEY
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found! Please set GOOGLE_API_KEY in Secrets.")
    st.stop()

# 🤖 Client
client = genai.Client(api_key=API_KEY)

# 🎨 UI
st.set_page_config(page_title="ApexGuard AI", layout="centered")

st.title("🛡️ ApexGuard AI")
st.subheader("🔍 Deepfake Detection System")

# 📤 Upload
uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        st.image(img, caption="📷 Uploaded Image", use_container_width=True)

        prompt = """
        Analyze this image and detect if it is deepfake.

        Give:
        - Score (0-100)
        - Verdict (Real / Fake)
        - Reason
        """

        with st.spinner("🧠 Scanning..."):
            response = client.models.generate_content(
                model="gemini-1.0-pro-vision",   # ✅ STABLE MODEL (IMPORTANT)
                contents=[prompt, img]
            )

        st.success("✅ Done")
        st.write(response.text)

    except Exception as e:
        st.error(f"❌ Error: {e}")

st.caption("⚡ Developed by Team The Apex AI")
