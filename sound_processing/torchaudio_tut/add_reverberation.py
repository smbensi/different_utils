import math
import os

import matplotlib.pyplot as plt
import requests
import torchaudio
import torch

from config import *
import utils

import time

sample_rate = 8000

rir_raw, _ = utils.get_rir_sample(resample=sample_rate)

utils.plot_waveform(rir_raw, sample_rate, title="Room Impulse Response (raw)",
                    ylim=None)
utils.plot_specgram(rir_raw, sample_rate, title="Room Impulse Response (raw)")

rir = rir_raw[:, int(sample_rate * 1.01) : int(sample_rate * 1.3)]
rir = rir / torch.norm(rir, p=2)
rir = torch.flip(rir, [1])

utils.print_stats(rir)
utils.plot_waveform(rir, sample_rate, title="Room Impulse Response",ylim=None)
utils.plot_specgram(rir, sample_rate, title="Room Impulse Response (raw)")

speech, _ = utils.get_speech_sample(resample=sample_rate)

speech_ = torch.nn.functional.pad(speech, (rir.shape[1] -1, 0))
augmented = torch.nn.functional.conv1d(speech_[None, ...], rir[None, ...])[0]

utils.plot_waveform(speech, sample_rate, title="Original", ylim=None)
utils.plot_specgram(speech, sample_rate, title="Original")
# play_audio(speech, sample_rate)

utils.plot_waveform(augmented, sample_rate, title="RIR Applied", ylim=None)
utils.plot_specgram(augmented, sample_rate, title="RIR Applied")
# play_audio(augmented, sample_rate)



