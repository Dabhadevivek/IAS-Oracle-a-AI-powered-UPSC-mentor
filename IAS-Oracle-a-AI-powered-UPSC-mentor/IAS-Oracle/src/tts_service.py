from gtts import gTTS
import pyttsx3
import os

def generate_audio_gtts(text, output_filename):
    tts = gTTS(text)
    tts.save(output_filename)
    print(f"Audio saved as {output_filename}")

def generate_audio_pyttsx3(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Usage with gTTS
text_to_convert = "Your summary of the news is ready."
output_file = "../audio_summaries/news_summary.mp3"
generate_audio_gtts(text_to_convert, output_file)

# Usage with pyttsx3
generate_audio_pyttsx3("Your assignment is ready.")