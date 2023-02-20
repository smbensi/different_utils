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

## clip audio with pydub

To trim audio data with `pydub`, we only need the `AudioSegment` object. To start, we'll define the first and last milliseconds we want to clip out. Then, we'll load the audio file with `AudioSegment`

To clip our audio file down, we'll create a list that only contains the data from the start to the end millisecond in our audio file. Finally, we'll use the `export` function of the `AudioSegment` object we extracted to save the file in `.wav` format

```python

from pydub import AudioSegment

# start at 0 ms end at 1500 ms
start = 0
end = 1500

sound = AudioSegment.from_wav("output_pyaudio.wav")
extract = sound[start:end]

extract.export("trimmed_output_pydub.wav", format="wav")

```

## Trim audio clips with FFMPEG

FFMPEG is a well known audio manipulation library, usually in CLI. You can use the `sys` and `subprocess` libraries that are native to Python to use FFMPEG, but the SDK is easier.
> to install : pip install ffmeg-python

We import it as just `ffmpeg`. The first thing we'll do is get an input object.
Then we'll use the `ffmpeg.input` object to call the `atrim` function and trim the recording down to 1 second. Next, we'll create an output using the newly cut data. Finally, we'll need to call `ffmpeg` to actually run the `output` call and save our file.

```python

import ffmpeg

audio_input = ffmpeg.input("output_sounddevice.wav")
audio_cut = audio_input.audio.filter('atrim', duration=1)
audio_output = ffmpeg.output(audio_cut, 'trimmed_output_ffmpeg.wav", format="wav")
ffmpeg.run(audio_output)
```


# Manipulating Audio Data sampling rates with Python

Sampling rates play a hug part in how audio data sounds. When you change it, it can affect the speed, the pitch, and the quality of your sound

## Pydub

The `AudioSegment` has a `set_frame_rate` command that can be used to set the frame rate of the audio segment without changing the pitch, speed, or applying any other distortions.

```python
from pydub import AudioSegment

sound = AudioSegment.from_wav('output_pyaudio.wav')
sound_w_new_fs = sound.set_frame_rate(16000)
sound_w_new_fs.export("new_fs_output_pydub.wav",format="wav")

```

## Scipy

Read in the sample rate and audio data using `wavfile`. Using the read-in sample rate and the desired new sample rate, create a new number of samples. The resample function applies a FFT and may cause distortion.
```python
from scipy.io import wavfile
import scipy.signal

new_fs = 88200
sample_rate, data = wavfile.read('output_pyaudio.wav')
# resample data
new_num_samples = round(len(data)* float(new_fs)/sample_rate)
data = scipy.signal.resample(data, new_num_samples)
wavfile.write(filename="new_fs_output_scipy.wav", rate=88200, data=data)

```

# Changing the Volume of audio data with Python

Changing volume with the `AudioSegment` object from `pydub` is extremely easy. The only thing we need to do is add or subtract from the object representing the open `.wav` file

```python
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav("new_fs_output_pydub.wav")

# 3 dB up
louder = sound + 3
# 3 dB down
quieter = sound - 3

play(louder)
play(quieter)

```

# Combining 2 audio files with Python
We can also use `pydub`

```python
from pydub import AudioSegment

sound1 = AudioSegment.from_wav('louder_output.wav')
sound2 = AudioSegment.from_wav('quieter_output.wav')
combined = sound1 + sound2

```

# Overlay 2 audio files
Call the `overlay` function in `pydub` and pass it the sound we wabt to overlay and the position in ms we want to overlay it at.

```python
from pydub import AudioSegment

sound1 = AudioSegment.from_wav('louder_output.wav')
sound2 = AudioSegment.from_wav('quieter_output.wav')

overlay = sound1.overlay(sound2, position=1000)
```

# Changing audio file formats
The `AudioSegment` object's `export` function can define the output object's format.

```python
from pydub import AudioSegment

wav_audio = AudioSegment.from_wav("louder_output.wav")
mp3_audio = wav_audio.export("louder.mp3", format="mp3")
```
