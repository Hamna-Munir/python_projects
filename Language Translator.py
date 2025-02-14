from tkinter import *
import googletrans
from googletrans import Translator
import speech_recognition as sr
import gtts
import os
import pygame

# Function to translate text
def translate_text():
    text = input_text.get("1.0", "end-1c")  # Get text from input box
    translator = Translator()
    translated = translator.translate(text, src="en", dest="tr")  # English to Turkish
    output_text.delete("1.0", "end")  # Clear previous text
    output_text.insert("1.0", translated.text)  # Insert translated text

# Function for voice input
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Listening...")
        root.update()  # Update UI
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for input
            text = recognizer.recognize_google(audio, language="en")  # Convert speech to text
            input_text.delete("1.0", "end")
            input_text.insert("1.0", text)  # Insert recognized text
        except sr.UnknownValueError:
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "Could not understand audio")
        except sr.RequestError:
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "Error connecting to Google Speech Recognition")

# Function for voice output (repeats audio multiple times)
def speak_translation():
    text = output_text.get("1.0", "end-1c")  # Get translated text
    if text:
        tts = gtts.gTTS(text, lang="tr")  # Convert text to speech
        tts.save("translated.mp3")  # Save as an audio file
        pygame.mixer.init()
        pygame.mixer.music.load("translated.mp3")
        
        # Play translation multiple times
        repeat_times = 3  # Change this number to control repetition
        for _ in range(repeat_times):
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait until playback is finished
                continue

# Create GUI window
root = Tk()
root.title("English to Turkish Translator")
root.geometry("450x400")
root.configure(bg="lightblue")

# Labels
Label(root, text="Enter English Text:", font=("Arial", 12), bg="lightblue").pack(pady=5)

# Input Text Box
input_text = Text(root, height=5, width=50)
input_text.pack(pady=5)

# Translate Button
Button(root, text="Translate", font=("Arial", 12), command=translate_text, bg="yellow").pack(pady=5)

# Voice Input Button
Button(root, text="🎤 Speak", font=("Arial", 12), command=voice_input, bg="green").pack(pady=5)

# Output Label
Label(root, text="Turkish Translation:", font=("Arial", 12), bg="lightblue").pack(pady=5)

# Output Text Box
output_text = Text(root, height=5, width=50)
output_text.pack(pady=5)

# Voice Output Button
Button(root, text="🔊 Hear Translation", font=("Arial", 12), command=speak_translation, bg="orange").pack(pady=5)

# Run the GUI
root.mainloop()