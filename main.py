from SpeechRecognition import audio_to_text
from vocal_recording import recording_audio
from order import order
from text_to_sound import text_to_speech
import os

start=True
text=""
while start:
	delet=True
	record=recording_audio(2)
	
	
	if audio_to_text(record):
		text=audio_to_text(record)
		if text.lower()=="jarvis":
			print("jarvis")
			text_to_speech("yes master")
			record=recording_audio(3)

			text=audio_to_text(record)
			split_list = text.split(" ")
			order(split_list)
			del record
			delet=False


	if delet:
		os.remove("records/"+record)
	if text.lower()=="stop":
		break  
		




	
