#Speech to text feature code

#Run this in the consol first :
#pip install sounddevice numpy scipy pydub keyboard
#Don't forget to install whisper
print("Initializing System")

import whisper

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment

import keyboard

import time

print("System Initialized")
print("Press SPACE to start recording")
print("Press ESC to exit")

# Set the parameters for recording
fs = 44100  # sample rate
max_duration = 30    
audio_data = []

recording = False
stop = False

def start_recording():

    print("Recording... Press SPACE to stop.")
     
    global audio_data
    audio_data = sd.rec(int(fs*max_duration), samplerate=fs, channels=2, dtype=np.int16, blocking=False)

def stop_recording():
    sd.stop()

    print("Recording stopped.")

def run():
    #audio_data = whisper.pad_or_trim(audio_data)
    wav_file_path = "recorded_audio.wav"

    print("Saving audio file")

    wav.write(wav_file_path, fs, audio_data)
    
    # Convert the WAV file to MP3
    mp3_file_path = "recorded_audio.mp3"

    print("Converting file to mp3")

    audio = AudioSegment.from_wav(wav_file_path)
    audio.export(mp3_file_path, format="mp3")

    print("Conversion complete.")

    model = whisper.load_model("base")
    result = model.transcribe("recorded_audio.mp3", verbose=True)
    print(result["text"])

def action():
    global recording

    if recording:
        recording = False
        stop_recording()
        run()
        print("Press SPACE to start recording")
        print("Press ESC to exit")
    else :
        recording = True
        start_recording()

def terminate():
    global stop
    stop = True

keyboard.add_hotkey('space', action)
keyboard.add_hotkey('esc', terminate)

while not stop:
    time.sleep(1)
print("System Terminated")