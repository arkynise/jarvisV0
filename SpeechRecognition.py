import speech_recognition as sr

def audio_to_text(audio_file):
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()
    audio_file="records/"+audio_file
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        # Extract audio data from the file
        audio_data = recognizer.record(source)

        try:
            # Recognize the audio and convert it to text
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Example usage
"""audio_file = "output.wav"
text = audio_to_text(audio_file)
print("Text from audio:", text)"""
