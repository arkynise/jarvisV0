import pyaudio
import wave
import datetime
import shutil
# Constants
def recording_audio(seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = seconds
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    date_string = current_date.strftime("%Y%m%d")
    time_string = current_time.strftime("%H%M%S")
    #OUTPUT_FILENAME = f"{date_string}_{time_string}.wav"
    OUTPUT_FILENAME="record_"+date_string+"_"+time_string+".wav"
    #print(OUTPUT_FILENAME)
# Initialize PyAudio
    audio = pyaudio.PyAudio()

# Open stream
    stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("Recording...")

    frames = []

# Record audio in chunks and save it to frames list
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("Finished recording.")

# Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

# Save the recorded audio to a file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    destination = "records/"

# Move the file
    shutil.move(OUTPUT_FILENAME, destination)
    #print("Audio recorded")
    return OUTPUT_FILENAME
    
