#!/usr/bin/env python3

from controller.main_controller import MainController
from view.main_view import MainView


def print_menu():
	print(34 * '#')
	print('# {0:<30} #'.format('Welcome to Terminal Bank!'))
	print(34 * '#')
	print('# {0:<30} #'.format(''))
	print('# {0:<30} #'.format('Choose an option:'))
	print('# {0:<30} #'.format('1 - Login'))
	print('# {0:<30} #'.format('0 - Close application'))
	print('# {0:<30} #'.format(''))
	print(34 * '#')
	print()
	print('Type your option:')

if __name__ == '__main__':
	
	view = MainView()
	controller = MainController(view)
	
	close_app = False
	while not close_app:
		view.clear()
		print_menu()
		if input() != '0':
			controller.start_session()
		else:
			close_app = True
	
	view.clear()



	#main_view.show_main_menu()
	


	
	

	
	

	#print(bank.name)
	#dal = BankDAL(bank)
	#dal.print_model()
