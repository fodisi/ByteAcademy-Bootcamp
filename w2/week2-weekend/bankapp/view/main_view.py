#!/usr/bin/env python3


from model.account import Account
from model.person import Person
from view.base_view import BaseView


class MainView(BaseView):

	def show_main_menu(self, profile):
		choice = 0
		
		self.clear()
		if profile == 'admin':
			self.show_admin_menu()
		elif isinstance(profile, Person):
			self.show_manager_menu(profile)
		elif isinstance(profile, Account):
			self.show_client_menu(profile)
		else:
			raise Exception('Invalid profile "{0}"'.format(profile))
			
		try:
			print('Your option:')
			choice = int(input())
		except Exception:
			print('Invalid option. Press ENTER to continue...') 
			input()
		
		return choice	
	
	def show_admin_menu(self):
		print(34 * '#')
		print('# {0:^30} #'.format('WELCOME'))
		print('# {0:^30} #'.format('Profile: ADMIN'))
		print(34 * '#')
		#Prints menu options
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('100 - Create Branch'))
		print('# {0:<30} #'.format('101 - View Branch List'))
		print('# {0:<30} #'.format('102 - Create Manager'))
		print('# {0:<30} #'.format('103 - View Manager List'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()

	def show_manager_menu(self, manager):
		print(34 * '#')
		welcome_message = 'WELCOME, {0}'.format(manager.name)
		print('# {0:^30} #'.format(welcome_message))
		print('# {0:^30} #'.format('Profile: MANAGER'))
		print(34 * '#')
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('200 - Create Account'))
		print('# {0:<30} #'.format('201 - View Account List'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()

	
	def show_client_menu(self, account):
		#Prints header
		print(34 * '#')
		welcome_message = 'WELCOME, {0}'.format(account.client.name)
		print('# {0:^30} #'.format(welcome_message))
		print(34 * '#')
		print('# {0:<30} #'.format("YOUR'RE CONNECTED TO:"))
		branch_info = 'Branch: {0:07d}'.format(account.branch_id)
		account_info = 'Account Number: {0:07d}'.format(account.number)
		print('# {0:<30} #'.format(branch_info))
		print('# {0:<30} #'.format(account_info))
		print(34 * '#')
		#Prints menu options
		print('# {0:<30} #'.format('Choose an option:'))
		print('# {0:<30} #'.format('1 - Deposit'))
		print('# {0:<30} #'.format('2 - Withdrawal'))
		print('# {0:<30} #'.format('3 - Account Balance'))
		print('# {0:<30} #'.format('4 - Transaction History'))
		print('# {0:<30} #'.format('0 - Exit'))
		print(34 * '#')
		print()









