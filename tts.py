import os
import uuid
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("IBM_API_KEY")
url = os.getenv("IBM_TTS_URL")

authenticator = IAMAuthenticator(api_key)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

def synthesize(text: str, voice: str = "en-US_AllisonV3Voice") -> str:
    filename = f"output_{uuid.uuid4().hex}.mp3"
    with open(filename, "wb") as audio_file:
        response = tts.synthesize(
            text=text,
            voice=voice,
            accept="audio/mp3"
        ).get_result()
        audio_file.write(response.content)
    return filename
