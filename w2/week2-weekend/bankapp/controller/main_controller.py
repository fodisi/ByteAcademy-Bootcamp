#!/usr/bin/env python3

from controller.branch_controller import BranchController
from controller.person_controller import PersonController
from controller.account_controller import AccountController
from view.main_view import MainView
from view.login_view import LoginView

class MainController():
	def __init__(self, view):
		self.view = view
	
	def start_session(self):
		user = self.login()
		if user == 'invalid':
			return
		
		option = 1
		while option > 0:
			option = self.view.show_main_menu(user)
			if option == 1:
				pass
			elif option == 2:
				pass
			elif option == 3:
				pass
			elif option == 4:
				pass
			elif option == 5:
				pass
			elif option == 100:
				BranchController().create_branch()
			elif option == 101:
				BranchController().list_branches()
			elif option == 102:
				PersonController().create_person('Manager')
			elif option == 103:
				PersonController().list_people('Manager')
			elif option == 200:
				AccountController().create_account()
			elif option == 201:
				AccountController().list_client_accounts()
		
	
	def login(self):
		user, password = LoginView().show_login()
		if user in ['admin', 'manager', 'client']:
			return user
		else:
			self.view.show_message('Error', 'Login invalid.', True)
			return 'invalid'
