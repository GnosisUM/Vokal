import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
from pydub import AudioSegment

st.set_page_config(
    page_title = 'Gnosis',
    page_icon = ":crocodile:",
    menu_items = {
        'Get Help': 'https://www.google.com/',
        'Report a bug': 'https://www.google.com/',
        'About': 
            "Submission by Team Gnosis for #BuildWithAI 2021 Hackathon Challenge 2"
    }
)

st.title('Gnosis')

st.set_page_config(page_title="Gnosis", layout="wide")

def convert_to_wav(non_wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export("wav_file.wav", format="wav")

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

def plot_waveform(file_name, files):
    for i in range(len(files)):
        if file_name == files[i].name:
            spf = wave.open(files[i], "r")

    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, "Int16")

    # If Stereo
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    plt.figure(1)
    plt.title("Signal Wave...")
    plt.plot(signal)
    plt.show()

st.title('Gnosis')

col1, col2 = st.columns(2)

# File uploader
with col1:
    uploaded_files = st.file_uploader(
        "Upload audio file(s)",
        type=['wav','mp3'],
        accept_multiple_files=True
    )

# Displays dropdown menu if number of files > 1
with col2:
    if len(uploaded_files) > 1:
        dropdown_selection = st.selectbox(
            "Choose audio file to play",
            get_file_names(uploaded_files),
            1
        )

        display_audio_playback(dropdown_selection, uploaded_files)
        plot_waveform(dropdown_selection, uploaded_files)

    # Displays only the audio player when number of files == 1
    if len(uploaded_files) == 1:
        st.audio(uploaded_files[0])    