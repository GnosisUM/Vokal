import streamlit as st
from pathlib import Path

st.header('Gnosis')

user_uploaded_audio = st.file_uploader("Upload an audio file (wav, mp3)")

def convert_to_wav(non_wav_file):
    pass

# function to compute audio using AI model
def compute_audio(wav_file):
    pass

if user_uploaded_audio:
    audio_bytes = user_uploaded_audio.read()
    st.audio(audio_bytes)