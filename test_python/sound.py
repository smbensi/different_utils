import sounddevice as sd
import soundfile as sf

volume = 0.5  # the volume level, between 0 and 1
sd.default.device = 0,0
# sd.default.channels = 2
# sd.default.samplerate = 44100
# sd.default.latency = 'low'
# sd.default.blocksize = 2048
# sd.default.dtype = 'float32'
# sd.default.extra_settings = None
# sd.default.clip_off = False
# sd.default.dither_off = False
# sd.default.never_drop_input = False
# sd.default.prime_output_buffers_using_stream_callback = False
# sd.default.high_latency = False
# sd.default.tweakable = False
# sd.default._silent = False
sd.default.volume = volume

filename = "test_python/stream0.wav"
data, fs = sf.read(filename, dtype='float64')
sd.play(data, fs)