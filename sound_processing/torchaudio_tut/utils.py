import math
import os

import matplotlib.pyplot as plt
import requests
import torchaudio
import torch

from config import *

def _fetch_data():
    uri = [(SAMPLE_WAV_URL, SAMPLE_WAV_PATH),
            (SAMPLE_RIR_URL, SAMPLE_RIR_PATH),
            (SAMPLE_WAV_SPEECH_URL, SAMPLE_WAV_SPEECH_PATH),
            (SAMPLE_NOISE_URL, SAMPLE_NOISE_PATH),
            ]
    for url, path in uri:
        with open(path, "wb") as file_:
            file_.write(requests.get(url).content)

def _get_sample(path, resample=None):
    effects = [["remix","1"]]
    if resample:
        effects.extend([
            ["lowpass",f"{resample//2}"],
            ["rate",f"{resample}"]
        ])
    return torchaudio.sox_effects.apply_effects_file(path, effects=effects)

def get_sample(*, resample=None):
    return _get_sample(SAMPLE_WAV_PATH, resample=resample)

def get_speech_sample(*, resample=None):
    return _get_sample(SAMPLE_WAV_SPEECH_PATH, resample=resample)

def plot_waveform(waveform, sample_rate, title="Waveform", xlim=None, ylim=None):
    waveform = waveform.numpy()
    num_channels, num_frames = waveform.shape
    time_axis = torch.arange(0, num_frames) / sample_rate

    figure, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].plot(time_axis, waveform[c], linewidth=1)
        axes[c].grid = True
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
        if xlim:
            axes[c].set_xlim(xlim)
        if ylim:
            axes[c].set_ylim(ylim)
    figure.suptitle(title)
    plt.show(block=False)

def print_stats(waveform, sample_rate=None, src=None):
    if src:
        print("-"*10)
        print(f"Source: {src}")
        print("-"*10)
    if sample_rate:
        print(f"Sample rate: {sample_rate}")
    print("Dtype:", waveform.dtype)
    print(f" - Max:     {waveform.max().item():6.3f}")
    print(f" - Min:     {waveform.min().item():6.3f}")
    print(f" - Mean:     {waveform.mean().item():6.3f}")
    print(f" - Std Dev:     {waveform.std().item():6.3f}")
    print()
    print(waveform)
    print()

def plot_specgram(waveform, sample_rate, title="Spectrogram", xlim=None):
    waveform = waveform.numpy()
    num_channels, num_frames = waveform.shape
    figure, axes = plt.subplots(num_channels, 1)
    if num_channels==1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].specgram(waveform[c], Fs=sample_rate)
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
        if xlim:
            axes[c].set_xlim(xlim)
    figure.suptitle(title)
    plt.show(block=False)

def get_rir_sample(*, resample=None, processed=False):
    rir_raw, sample_rate = _get_sample(SAMPLE_RIR_PATH, resample=resample)
    if not processed:
        return rir_raw, sample_rate
    rir = rir_raw[:, int(sample_rate*1.01) : int(sample_rate*1.3)]
    rir = rir / torch.norm(rir, p=2)
    rir = torch.flip(rir, [1])
    return rir, sample_rate

def get_noise_sample(*, resample=None):
    return _get_sample(SAMPLE_NOISE_PATH, resample=resample)

