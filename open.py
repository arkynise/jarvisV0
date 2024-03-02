import os
from text_to_sound import text_to_speech
def concat_order(word_list):
	text=""
	for string in word_list:
		text =text+string+" "
	return text

def open(order):

	files_in_directory = os.listdir("C:/Users/PC/Desktop/logiciel")
	found=False
	for file_name in files_in_directory:
		split=file_name.split(".")
		split = split[:-1]
		lowercase_list = [string.lower() for string in split]
		splited_list = [string.split(" ") for string in lowercase_list]
		flat_list=[]
		[flat_list.extend(sublist) for sublist in splited_list]
		#print(flat_list)
		order_lowercase = [string.lower() for string in order]
		if flat_list==order_lowercase:
			os.startfile("C:/Users/PC/Desktop/logiciel/"+file_name)
			found=True

	if not found:
		order_lowercase = [string.lower() for string in order]
		text_to_speech("i didn't find file with name "+concat_order(order_lowercase))
	if found:
		order_lowercase = [string.lower() for string in order]

		text_to_speech(concat_order(order_lowercase)+" is opened")
 
			
	

	"""try:
		softwar=order[0]+".lnk"
		print(len(order))
		os.startfile("C:/Users/PC/Desktop/logiciel/"+softwar)
	except Exception as e:
		print(f"Error: {e}")"""