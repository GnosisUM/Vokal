import streamlit as st
import pandas as pd
from pathlib import Path

def convert_to_wav(non_wav_file):
    pass

# function to compute audio using AI model
def compute_audio(wav_file):
    pass

# function to get filename from a list
def get_file_names(files):
    file_names = []
    for i in range(len(files)):
        file_names.append(files[i].name)
    return file_names

# function to display audio player based on dropdown selection
def display_audio_playback(file_name, files):
    for i in range(len(files)):
        if file_name == files[i].name:
            st.audio(files[i])

st.header('Gnosis')

# File uploader
uploaded_files = st.file_uploader(
    "Upload audio file(s)",
    type=['wav','mp3'],
    accept_multiple_files=True
)

# Displays dropdown menu if number of files > 1
if len(uploaded_files) > 1:
    dropdown_selection = st.selectbox(
        "Choose audio file to play",
        get_file_names(uploaded_files),
        1
    )

    display_audio_playback(dropdown_selection, uploaded_files)

# Displays only the audio player when number of files == 1
if len(uploaded_files) == 1:
    st.audio(uploaded_files[0])