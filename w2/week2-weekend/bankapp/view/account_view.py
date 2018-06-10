#!/usr/bin/env python3


from view.base_view import BaseView
from model.account import Account
from model.client import Client


class AccountView(BaseView):
	
	def create_account(self):
		self.clear()
		data = {}
		try:
			print(34 * '#')
			print('# {0:<30} #'.format('Create New Account:'))
			print(34 * '#')
			print()
			#TODO - Validate number and branch_id for integer input
			print('Type the branch id (only numbers):')
			data['branch_id'] = int(input())
			print('Type the account number (only numbers):')
			data['number'] = int(input())
			print('Type the client name:')
			data['name'] = input()
			print('Type the client email:')
			data['email'] = input()
			print('Type the client login:')
			data['login'] = input()
			print('Type the client password:')
			data['password'] = input()
			
			return data
		except Exception as e:
			self.view.show_message('Error', e.args[0], True)

	def view_client_accounts(self, accounts):
		self.clear()
		print(80 * '#')
		print('# {0:<76} #'.format('List of Client Accounts:'))
		print(80 * '#')
		print('# {0:<76} #'.format(''))
		pattern = '# {0:<7} | {1:<7} | {2:<7} | {3:<15} | {4:<15} | {5:<10} #'
		print(pattern.format('Branch',
							 'Account',
							 'Cli. Id',
							 'Name',
							 'Email',
							 'Login'
							))
		
		pattern = '# {0:07d} | {1:07d} | {2:07d} | {3:<15} | {4:<15} | {5:<10} #'
		for account in accounts:
			print(pattern.format(account.branch_id,
								 account.number,
								 account.client.id,
								 account.client.name,
								 account.client.email,
								 account.client.login
								))
		
		print('# {0:<76} #'.format(''))
		print(80 * '#')
		print('\n\nPress ENTER to return:')
		return input()
