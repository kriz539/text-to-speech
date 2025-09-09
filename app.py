import streamlit as st
from tts import synthesize
from tone_rewriter import rewrite_text
from utils import read_uploaded_file
import os

st.set_page_config(page_title="EchoVerse – Audiobook Generator", layout="wide")

st.title("🎧 EchoVerse – AI Audiobook Creator")

st.sidebar.header("🔧 Settings")
tone = st.sidebar.selectbox("Choose Tone", ["Neutral", "Suspenseful", "Inspiring"])
voice = st.sidebar.selectbox("Choose Voice", {
    "Allison (Female, US)": "en-US_AllisonV3Voice",
    "Lisa (Female, US)": "en-US_LisaV3Voice",
    "Michael (Male, US)": "en-US_MichaelV3Voice"
}.keys())

st.sidebar.markdown("---")

# Input section
st.subheader("📄 Input Text")
input_method = st.radio("Input Method", ["Paste Text", "Upload .txt File"])

if input_method == "Paste Text":
    original_text = st.text_area("Enter your text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    original_text = ""
    if uploaded_file:
        original_text = read_uploaded_file(uploaded_file)

# Process Button
if st.button("🔁 Generate Audio"):
    if not original_text.strip():
        st.error("Please enter or upload text first.")
    else:
        with st.spinner("🔄 Rewriting text..."):
            adapted_text = rewrite_text(original_text, tone)

        st.subheader("📝 Text Comparison")
        col1, col2 = st.columns(2)
        col1.text_area("Original Text", original_text, height=200)
        col2.text_area(f"{tone} Tone Text", adapted_text, height=200)

        with st.spinner("🎙 Generating speech..."):
            audio_file = synthesize(adapted_text, voice={
                "Allison (Female, US)": "en-US_AllisonV3Voice",
                "Lisa (Female, US)": "en-US_LisaV3Voice",
                "Michael (Male, US)": "en-US_MichaelV3Voice"
            }[voice])

        st.audio(audio_file, format="audio/mp3")
        with open(audio_file, "rb") as f:
            st.download_button("⬇️ Download Audio", f, "echoverse_output.mp3", mime="audio/mp3")

        # Clean up
        os.remove(audio_file)
