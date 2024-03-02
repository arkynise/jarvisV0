import os
from open import open
from create import create
from search import search
from close import close
from text_to_sound import text_to_speech


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
		text_to_speech("understod, i will turn off, feel free to call me when you need me master")
	else:
		text_to_speech("i didn't understand the command")


		