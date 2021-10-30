import streamlit as st
import pandas as pd
from pathlib import Path

def convert_to_wav(non_wav_file):
    pass

# function to compute audio using AI model
def compute_audio(wav_file):
    pass

def get_file_names(files):
    file_names = []
    for i in range(len(files)):
        file_names.append(files[i].name)
    return file_names

st.header('Gnosis')

uploaded_files = st.file_uploader("Upload an audio file (wav, mp3)", type=['wav','mp3'], accept_multiple_files=True)


st.selectbox(
    "Choose audio file to play",
    get_file_names(uploaded_files)
)
