#!/usr/bin/env python3

from controller.main_controller import MainController
from view.base_view import BaseView


def print_menu():
	print(34 * '#')
	#TODO center main main
	print('# {0:^30} #'.format('WELCOME TO TERMINAL BANK'))
	print(34 * '#')
	print('# {0:<30} #'.format(''))
	print('# {0:<30} #'.format('Choose an option:'))
	print('# {0:<30} #'.format('1 - Login'))
	print('# {0:<30} #'.format('0 - Close'))
	print('# {0:<30} #'.format(''))
	print(34 * '#')
	print()
	print('Type your option:')

if __name__ == '__main__':
	
	controller = MainController()
	
	close_app = False
	while not close_app:
		BaseView.clear_screen()
		print_menu()
		choice = input()
		if choice == '0':
			close_app = True
		elif choice == '1':
			controller.start_session()
		else:
			BaseView.clear_screen()
			print('\nInvalid option.\n')
			print('Press ENTER to try again...')
			input()
			
	
	BaseView.clear_screen()
