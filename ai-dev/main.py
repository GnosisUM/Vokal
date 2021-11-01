from diarizer import Diarizer

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import soundfile as sf

def to_df(segments):
    start = [segment['start'] for segment in segments]
    end = [segment['end'] for segment in segments]
    label = [segment['label'] for segment in segments]
    start_sample = [segment['start_sample'] for segment in segments]
    end_sample = [segment['end_sample'] for segment in segments]
    
    dictionary = {
        'start': start, 
        'end' : end,
        'label': label,
        'start_sample': start_sample,
        'end_sample': end_sample
    }
    return pd.DataFrame(dictionary)

def run_diarization(WAV_FILE: str, embed_model: str, cluster_method: str) -> pd.DataFrame:
    """"
    Run speaker diarization.
    params:
        WAV_FILE: The name of the audio file
        embed_model: The model name to extract embeddings (supported types: ['xvec', 'ecapa'])
        cluster_method: The model name to cluster embeddings (supported types: ['ahc', 'sc'])

    Returns:
        The dataframe of the diarization (start, end, label, start_sample, end_sample)
    """

    signal, sr = sf.read(WAV_FILE)

    diar = Diarizer(
                    embed_model='xvec', # supported types: ['xvec', 'ecapa']
                    cluster_method='sc', # supported types: ['ahc', 'sc']
                    window=1.5, # size of window to extract embeddings (in seconds)
                    period=0.75 # hop of window (in seconds)
                    )

    segments = diar.diarize(WAV_FILE, 
                            threshold=2.5,
                            outfile='test.rttm')

    return to_df(segments)
