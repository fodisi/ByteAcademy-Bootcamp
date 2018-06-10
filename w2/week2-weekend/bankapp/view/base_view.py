#!/usr/bin/env python3


import os

class BaseView():

	@staticmethod
	def clear_screen():
		os.system('cls' if os.name=='nt' else 'clear')

	def clear(self):
		BaseView.clear_screen()
	
	def show_message(self, title, message, clean_screen = False):
		if clean_screen == True:
			BaseView.clear_screen()
		
		print('{0}:\n{1}\n'.format(title, message))
		print('Press ENTER to continue...')
		input()

	#def input_integer(self, error_message, try_again_on_error)
	#	value = input()
	#	if value.isdigit():
			
