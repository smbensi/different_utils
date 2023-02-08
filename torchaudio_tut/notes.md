# Introduction to Audio data 
> [link](https://blog.deepgram.com/best-python-audio-manipulation-tools/)

### sampling rate
number of times per second that we measure the amplitude of the signal. It is measured in frames per second or Hertz (Hz). An ideal rate can be determined using Nyquist's Sampling Theorem. Some common sampling rates are 16 KkHz, 44.1kHz, and 96kHz

### Types of audio data

computers can represent that data in many ways most common are `.mp3` and `.wav`:
* `wav` are not compressed so great when you need the highest quality audio 
* `mp3` are compressed so best when you need fast streaming \
other format are : raw Pulse Code Manipulation(PCM), Advanced Audio Coding(AAC) (popular streaming audio format used by YouTube, IPhones,..)

### Recoding Audio Data with Python

how to record audio data with `sounddevice` and `pyaudio` . PyAudio is a wrapper around PortAudio.

### use PyAudio to Record Sound 

the constants we need to declare up front are the chunk size (the number of frames saved at a time), the format (16bit), the number of channels(1), the sampling rate (44100), the length of our recording (3 sec) and the filename

We create a PyAudio object. We'll use this object to create a stream with the constants set above. Then we'll initialize an empty list of frames to hold the frames. Next. we'll use the stream to read data while we still have time left in our 3 second timeframe and save it in the chunk size of 1024 bits.

We need to close and terminate our stream after 3 seconds. Finally we'll use the `wave` library to save the streamed audio data into a `.wav` file

```python
import pyaudio
import wave

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100 # frames per channel
seconds = 3
filename = "output_pyaudio.wav"

p = pyaudio.PyAudio()

print("recording...")

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []
for i in range(0, int(fs/chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print(" ... Ending Recording")
with wave.open(filename, "wb") as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes)b''.join(frames)
    wf.close()

```

### Record with Python-Sounddevice

It's a simple sound recording and playing library. we'll use the write function from `scipy.io.wavfile`. Next, we'll declare a couple constants for the sampling rate and the length of recording

```python
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 3

recording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait()
write('output_sounddevice.wav', fs, recording)

```

### Playing Audio with Python

we'll need one more library for using `sounddevice` to play audio data `soundfile`

### Use Pyaudio to play Audio

We'll start by opening the file and creating a pyaudio object
we'll will then use the pyaudio object to open a stream with specifications extracted from the wave file. Next, we'll create a data object that reads the frames on the wave file in the specified chunk size. To play the sound, we'll loop through the data file and write it to the stream while it is not an empty bit

```python
import pyaudio
import wave

# declare constants and initialize portaudio/pyaudio object
filename = 'output_pyaudio.wav'
chunk = 1024
wf = wave.open(filename, 'rb')
pa = pyaudio.PyAudio()

# create stream using info from the file
stream = pa.open(format = pa.get_format_from_widthwf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate = wf.getframerate(),
                    output=True)

# read in the frames as data
data = wf.readframes(chunk)

# while the data isn't empty
while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)

# cleanup
stream.close()
pa.terminate()

```

### Play audio with Python-sounddevice

```python
import sounddevice
import soundfile

filename = 'output_sounddevice.wav'
data, fs = soundfile.read(filename,dtype='float32')
sounddevice.play(data, fs)
status = sounddevice.wait()
```

# Clipping audio data with python

Let's move onto how to change the audio data. The first thing we'll cover is clipping or trimming audio data. We'll need 2 more libraries, `pydub` and `ffmpeg-python`

### clip audio with pydub

To trim audio data with `pydub`, we only need the `AudioSegment` object. To start, we'll define the first and last milliseconds we want to clip out. Then, we'll load the audio file with `AudioSegment`

# Tutorial torchaudio

* on peut ajouter des effets sur des wav grace a `sox` il existe une liste dans la doc de [sox](https://sox.sourceforge.net/sox.html) et en utilisant la fonction `sox_effects.apply_effects_tensor` elle returne 2 valeurs **waveform** et **new sample rate**

