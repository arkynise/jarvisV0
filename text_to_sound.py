from gtts import gTTS
from io import BytesIO
import os
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text):
	

	language = 'en'

	tts = gTTS(text=text, lang=language)

# Save the audio to a byte stream
	audio_stream = BytesIO()
	tts.write_to_fp(audio_stream)
	audio_stream.seek(0)


	audio_segment = AudioSegment.from_file(audio_stream, format="mp3")


	play(audio_segment)

