import streamlit as st
import google.generativeai as genai

# --- Step 1: Google Gemini Setup ---
GOOGLE_API_KEY = "AIzaSyDnVFu-OtG5_fCElU-MrsTI-OgVBUKbHBk" 

genai.configure(api_key=GOOGLE_API_KEY)
# यहाँ हमने मॉडल का नाम अपडेट किया है ताकि 404 एरर न आए
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

# --- Step 2: Website UI ---
st.set_page_config(page_title="The Apex AI - Deepfake Guard", page_icon="🛡️")

st.title("🛡️ ApexGuard AI")
st.subheader("Detecting Deepfakes & Digital Fraud in Real-Time")
st.write("Our AI analyzes micro-expressions and voice patterns to protect you from fraud.")

language = st.sidebar.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi"])

uploaded_file = st.file_uploader("Upload Audio, Video or Image", type=['mp4', 'mov', 'wav', 'mp3', 'jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.info("🔄 Scanning File with Gemini AI... Please wait.")
    
    try:
        if language == "English":
            prompt = "Act as a cyber-security expert. Analyze this media. Is it a Deepfake or AI-generated fraud? Check for unnatural movements and robotic patterns. Give a Safety Score (0-100)."
        else:
            prompt = "एक साइबर सुरक्षा विशेषज्ञ के रूप में कार्य करें। इस मीडिया का विश्लेषण करें। क्या यह डीपफेक या AI-जनरेटेड फ्रॉड है? सेफ्टी स्कोर (0-100) दें।"

        file_data = uploaded_file.getvalue()
        mime_type = uploaded_file.type
        
        # API Call
        response = model.generate_content([
            prompt,
            {'mime_type': mime_type, 'data': file_data}
        ])
        
        st.success("✅ Analysis Complete!")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.caption("Developed by Team The Apex AI | Goal 16: Peace & Justice")
