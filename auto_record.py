import pyaudio
import wave
import speech_recognition as sr
import threading

# Set parameters for audio recording
FORMAT = pyaudio.paInt16  # Sample size and format
CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100              # Sample rate (samples per second)
CHUNK = 1024              # Buffer size
RECORD_SECONDS = 5        # Duration of recording in seconds
OUTPUT_FILENAME = "output.wav"  # Output file name

# Function to continuously update the displayed text with recognized speech
def display_text():
    while True:
        try:
            text = q.get_nowait()
            print("You said:", text)
        except queue.Empty:
            pass

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream for audio input
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# Initialize SpeechRecognizer
recognizer = sr.Recognizer()

# Create a queue for communication between threads
import queue
q = queue.Queue()

# Create and start a thread for displaying recognized speech
display_thread = threading.Thread(target=display_text)
display_thread.daemon = True
display_thread.start()

print("Recording...")

frames = []

# Record audio for the specified duration
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    
    # Recognize speech in the audio data
    audio_data = sr.AudioData(data, RATE, 2)
    try:
        text = recognizer.recognize_google(audio_data)
        q.put(text)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))

print("Recording stopped.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print("Audio saved to:", OUTPUT_FILENAME)
