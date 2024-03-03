from PIL import Image
from docx import Document
from pptx import Presentation
import os
from color import write_color
from text_to_sound import text_to_speech


def create_path(order):
	new_directory_path="C:/Users/PC/Desktop/"
	for i in range(1,len(order)):
			new_directory_path=new_directory_path+order[i]
			if i<len(order)-1:
				new_directory_path=new_directory_path+" "
	return new_directory_path


def create(order):
	
	found=False
	new_directory_path=create_path(order)

	if order[0]=="directory":
		os.makedirs(new_directory_path, exist_ok=True)
		found=True



	if order[0].lower()=="image":
		
		new_image = Image.new('RGB', (500, 500), color='white')
		new_image.save(new_directory_path+".png")
		found=True


	if order[0].lower()=="word":
		
		doc = Document()

		doc.save(new_directory_path+'.docx')
		found=True


	if order[0].lower()=="powerpoint":
		presentation = Presentation()
		
		presentation.save(new_directory_path+'.pptx')
		found=True


	if order[0].lower()=="text":
		
		with open(new_directory_path+".txt", 'w') as file:
			found=True
	

	write_color("0,255,0")
	if not found:
		name=""
		for i in range(1,len(order)):
			name=name+order[i]
		text_to_speech("i couldn't create "+order[0].lower()+" "+name)
	else:
		name=""
		for i in range(1,len(order)):
			name=name+order[i]
		text_to_speech(order[0].lower()+" "+name+" created, you can find it in desktop")
	write_color("200,0,0")
		

    


		
	
