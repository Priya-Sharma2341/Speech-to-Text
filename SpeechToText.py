import io
from google.cloud import speech_v1p1beta1 as speech

client = speech.SpeechClient()

# The name of the audio file to transcribe
audio_file = 'Test.wav'

# Read the audio file into memory
with io.open(audio_file, 'rb') as f:
    content = f.read()

# Configure the speech recognition request
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US'
)

# Perform the speech recognition
audio = speech.RecognitionAudio(content=content)
response = client.recognize(config=config, audio=audio)

# Print the transcription
for result in response.results:
    print(result.alternatives[0].transcript)