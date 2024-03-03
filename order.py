import os
from open import open
from create import create
from search import search
from close import close
from text_to_sound import text_to_speech
from color import write_color


def order(order):

	order_lower_case = order[0].lower() 
	if(order_lower_case=="open"):
		order.pop(0)
		open(order)
	elif order_lower_case=="create":
		order.pop(0)
		create(order)

	elif order_lower_case=="search":
		order.pop(0)
		search(order)

	elif order_lower_case=="close":
		order.pop(0)
		close(order)
	elif order_lower_case=="stop":
		write_color("0,255,0")
		text_to_speech("understood, i will turn off, feel free to call me when you need me master")
		write_color("255,0,0")
	else:
		write_color("0,255,0")
		text_to_speech("i didn't understand the command")


		