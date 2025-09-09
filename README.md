# EchoVerse 🎧

EchoVerse is a generative AI audiobook creation system that:

- Accepts pasted or uploaded text
- Rewrites it in a custom tone (Neutral, Suspenseful, or Inspiring)
- Converts the result into expressive speech using IBM Watson TTS
- Allows streaming and downloading of the final MP3

## 🚀 Setup Instructions

1. Clone the repo
2. Create `.env` with your IBM Watson credentials
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
