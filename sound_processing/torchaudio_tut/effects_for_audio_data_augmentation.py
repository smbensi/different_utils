import math
import os

import matplotlib.pyplot as plt
import requests
import torchaudio
import torch

_SAMPLE_DIR = "_assets"
SAMPLE_WAV_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/steam-train-whistle-daniel_simon.wav"
SAMPLE_WAV_PATH = os.path.join(_SAMPLE_DIR, "steam.wav")

SAMPLE_RIR_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/VOiCES_devkit/distant-16k/room-response/rm1/impulse/Lab41-SRI-VOiCES-rm1-impulse-mc01-stu-clo.wav"  # noqa: E501
SAMPLE_RIR_PATH = os.path.join(_SAMPLE_DIR, "rir.wav")

SAMPLE_WAV_SPEECH_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/VOiCES_devkit/source-16k/train/sp0307/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav"  # noqa: E501
SAMPLE_WAV_SPEECH_PATH = os.path.join(_SAMPLE_DIR, "speech.wav")

SAMPLE_NOISE_URL = "https://pytorch-tutorial-assets.s3.amazonaws.com/VOiCES_devkit/distant-16k/distractors/rm1/babb/Lab41-SRI-VOiCES-rm1-babb-mc01-stu-clo.wav"  # noqa: E501
SAMPLE_NOISE_PATH = os.path.join(_SAMPLE_DIR, "bg.wav")

os.makedirs(_SAMPLE_DIR, exist_ok=True)

def _fetch_data():
    uri = [(SAMPLE_WAV_URL, SAMPLE_WAV_PATH),
            (SAMPLE_RIR_URL, SAMPLE_RIR_PATH),
            (SAMPLE_WAV_SPEECH_URL, SAMPLE_WAV_SPEECH_PATH),
            (SAMPLE_NOISE_URL, SAMPLE_NOISE_PATH),
            ]
    for url, path in uri:
        with open(path, "wb") as file_:
            file_.write(requests.get(url).content)

_fetch_data()

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


# Load the data
waveform1, sample_rate1 = get_sample(resample=16000)

# Define effects
effects = [
    ["lowpass", "-1", "300"], # apply single-pole lowpass filter
    ["speed", "0.8"],   # reduce the speed
    # This only changes the sample rate, so it is necessary to
    # add `rate` effect with original sample rate after this
    ["rate", f"{sample_rate1}"],
    ["reverb", "-w"], # reverbation gives some dramatic feeling
]

# Apply effects
waveform2, sample_rate2 = torchaudio.sox_effects.apply_effects_tensor(waveform1,sample_rate1, effects)
print_stats(waveform1, sample_rate1, src="Original")
print_stats(waveform2, sample_rate2, src="Effects Applied")
plot_waveform(waveform1, sample_rate1, title="Original", xlim=(-0.1,3.2))
plot_specgram(waveform1, sample_rate1, title="Original", xlim=(0,3.04))
plot_waveform(waveform2, sample_rate2, title="Effects Applied", xlim=(-0.1,3.2))
# plot_specgram(waveform2, sample_rate2, title="Effects Applied", xlim=(0,3.04))



#  Adding Background noise

sample_rate = 8000
speech, _ = get_speech_sample(resample=sample_rate)
noise, _ = get_noise_sample(resample=sample_rate)
noise = noise[: , : speech.shape[1]]

speech_power = speech.norm(p=2)
noise_power = noise.norm(p=2)

snr_dbs = [20,10,3]
noisy_speech = []
for snr_db in snr_dbs:
    snr = math.exp(snr_db / 10)
    scale = snr * noise_power / speech_power
    noisy_speech.append((scale * speech + noise) / 2)
    
plot_waveform(noise, sample_rate, title="Background noise")
plot_specgram(noise, sample_rate, title="Background noise")

# background noise at certain levels
snr_db20, noisy_speech20 = snr_dbs[0], noisy_speech[0]
plot_waveform(noisy_speech20, sample_rate, title=f"SNR: {snr_db20} [dB]")
plot_specgram(noisy_speech20, sample_rate, title=f"SNR: {snr_db20} [dB]")

snr_db10, noisy_speech10 = snr_dbs[1], noisy_speech[1]
plot_waveform(noisy_speech10, sample_rate, title=f"SNR: {snr_db10} [dB]")
plot_specgram(noisy_speech10, sample_rate, title=f"SNR: {snr_db10} [dB]")

snr_db3, noisy_speech3 = snr_dbs[2], noisy_speech[2]
plot_waveform(noisy_speech3, sample_rate, title=f"SNR: {snr_db3} [dB]")
plot_specgram(noisy_speech3, sample_rate, title=f"SNR: {snr_db3} [dB]")


