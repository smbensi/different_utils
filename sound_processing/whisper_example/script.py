import whisper

model = whisper.load_model("base")

# run transcription
result = model.transcribe("./audio_sample.wav")
print(result["text"])

# save the resulting transcription to a text file
with open("audio_sample.txt", "w+") as f:
    f.write(result["text"])
