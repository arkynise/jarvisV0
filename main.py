from SpeechRecognition import audio_to_text
from vocal_recording import recording_audio
from order import order
from text_to_sound import text_to_speech
import os
from color import write_color
import subprocess
import psutil
from check_internet import check_internet_connection,error_window


def stop_subprocess(process):
    if process.poll() is None:  # Check if the process is still running
        parent = psutil.Process(process.pid)
        for child in parent.children(recursive=True):
            child.kill()  # Kill all child processes
        parent.kill()

def isConnected():
	connected=check_internet_connection()

	while not connected:
		error_window()
		connected=check_internet_connection()
		if connected:
			break





write_color("200,0,0")
isConnected()
#sub_process=subprocess.Popen(["python", "the_face.py"])



start=True
text=""
write_color("0,255,0")
text_to_speech("welcome back master, how can i help you today")





while start:
	
	delet=True
	write_color("255,0,0")
	record=recording_audio(3)
	write_color("200,0,0")
	text=audio_to_text(record)
	os.remove("records/"+record)


	
	if text:
		
		
		if "jarvis" in text.lower():

			write_color("0,255,0")
			text_to_speech("yes master")
			write_color("0,0,255")
			record=recording_audio(3)

			text=audio_to_text(record)

			if text is not None :
				split_list = text.split(" ")
				order(split_list)
				del record
				delet=False
			else:
				text_to_speech("you need to say the command before 4 seconds")
				write_color("255,0,0")
				os.remove("records/"+record)
			
			
			
			if text is not None and text.lower() =="stop":
				for proc in psutil.process_iter(['pid', 'name']):
					if proc.info['name'] == 'jarvis_0.1.exe':
						pid = proc.pid
						proc.terminate()

				break 


	 
		




	
