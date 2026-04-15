import streamlit as st
import google.generativeai as genai

# --- Step 1: Google Gemini Setup ---
# Your integrated API Key
GOOGLE_API_KEY = "AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk" 

genai.configure(api_key=GOOGLE_API_KEY)

# Latest Model Name to avoid 404 errors
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Step 2: Website UI (ApexGuard) ---
st.set_page_config(page_title="The Apex AI - Deepfake Guard", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Detecting Deepfakes & Digital Fraud in Real-Time")
st.write("Our AI analyzes micro-expressions and voice patterns to protect you from fraud.")

# Sidebar for Language Selection
language = st.sidebar.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi"])

# File Uploader
uploaded_file = st.file_uploader("Upload Audio, Video or Image", type=['mp4', 'mov', 'wav', 'mp3', 'jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Scanning File with Gemini AI... Please wait.")
    
    try:
        # Expert Prompt
        if language == "English":
            prompt = "Act as a cyber-security expert. Analyze this media. Is it a Deepfake or AI-generated fraud? Check for unnatural movements and robotic voice patterns. Give a Safety Score (0-100) and explain why."
        else:
            prompt = "एक साइबर सुरक्षा विशेषज्ञ के रूप में कार्य करें। इस मीडिया का विश्लेषण करें। क्या यह डीपफेक या AI-जनरेटेड फ्रॉड है? चेहरे के हाव-भाव और आवाज़ की जांच करें। इसे 0 से 100 के बीच सेफ्टी स्कोर दें और कारण बताएं।"

        # Correct way to send file data to Gemini 1.5
        file_details = {
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }
        
        response = model.generate_content([prompt, file_details])
        
        st.success("✅ Analysis Complete!")
        st.markdown("### 📊 Apex Analysis Result:")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Analysis failed: {e}")

st.divider()
st.caption("Developed by Team The Apex AI | Goal 16: Peace & Justice")


   
