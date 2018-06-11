#!/usr/bin/env python3


from datetime import datetime

from view.base_view import BaseView
from model.account import Account
from model.client import Client
from model.transaction import Transaction


class AccountView(BaseView):
	
	def create_account(self):
		self.clear()
		data = {}
		try:
			print(34 * '#')
			print('# {0:^30} #'.format('CREATE NEW ACCOUNT'))
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
		print('# {0:^76} #'.format("CLIENT ACCOUNT LIST"))
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


	def create_transaction(self, tx_type):
		self.clear()
		data = {}
		try:
			print(34 * '#')
			print('# {0:^30} #'.format(tx_type.upper()))
			print(34 * '#')
			print()
			#TODO - Validate date and amout for type before conversion
			#and allow user to try again
			print('Type the date (use formar YYYY/MM/DD):')
			data['date'] = datetime.strptime(input(), '%Y/%m/%d')
			
			print('Type a description for the transaction:')
			data['description'] = input()
			
			print('Type the amount:')
			data['amount'] = float(input())
			
			return data
		except Exception as e:
			self.show_message('Error', e.args[0], True)


	def view_statement(self, account):
		self.clear()
		#PRINTS HEADER
		print(74 * '#')
		print('# {0:^70} #'.format('ACCOUNT STATEMENT'))
		print(74 * '#')
		branch_info = 'Branch: {0:>10}{1:07d}'.format('', account.branch_id)
		account_info = 'Account Number: {0:>2}{1:07d}'.format('', account.number)
		client_info = 'Client: {0:>10}{1:<}'.format('', account.client.name)
		date_info = 'Date: {0:>12}{1:<}'.format('', datetime.now().strftime('%Y/%m/%d'))
		print('# {0:<70} #'.format(branch_info))
		print('# {0:<70} #'.format(account_info))
		print('# {0:<70} #'.format(client_info))
		print('# {0:<70} #'.format(date_info))
		print(74 * '#')
		#PRINTS TABLE HEADER
		pattern = '# {0:<15} | {1:<25} | {2:^6} | {3:>15} #'
		print(pattern.format('Date',
							 'Description',
							 'Type',
							 'Amount'
							))
		#PRINTS TABLE DETAILSA
		pattern = '# {0:<15} | {1:<25} | {2:^6} | {3:>15} #'
		for tx in account.get_transaction_history():
			print(pattern.format(tx.date.strftime('%Y/%m/%d'),
								 tx.description,
								 tx.type_,
								 '{0:.2f}'.format(tx.amount)
								))
		print(74 * '#')
		#PRINTS BALANCE
		print('# {0:<70} #'.format(''))
		balance = account.get_balance()
		balance_str = 'TOTAL BALANCE: {0:.2f}'.format(balance)
		print('# {0:>70} #'.format(balance_str))
		print('# {0:<70} #'.format(''))
		print(74 * '#')
		# ASKS FOR INPUT TO CONTINUE
		print('\n\nPress ENTER to return:')
		return input()


	def view_balance(self, account):
		self.clear()
		#PRINTS HEADER
		print(54 * '#')
		print('# {0:^50} #'.format('ACCOUNT BALANCE'))
		print(54 * '#')
		branch_info = 'Branch: {0:>10}{1:07d}'.format('', account.branch_id)
		account_info = 'Account Number: {0:>2}{1:07d}'.format('', account.number)
		client_info = 'Client: {0:>10}{1:<}'.format('', account.client.name)
		date_info = 'Date: {0:>12}{1:<}'.format('', datetime.now().strftime('%Y/%m/%d'))
		print('# {0:<50} #'.format(branch_info))
		print('# {0:<50} #'.format(account_info))
		print('# {0:<50} #'.format(client_info))
		print('# {0:<50} #'.format(date_info))
		print(54 * '#')
		#PRINTS BALANCE
		print('# {0:<50} #'.format(''))
		balance = account.get_balance()
		balance_str = 'TOTAL BALANCE: {0:.2f}'.format(balance)
		print('# {0:>50} #'.format(balance_str))
		print('# {0:<50} #'.format(''))
		print(54 * '#')
		# ASKS FOR INPUT TO CONTINUE
		print('\n\nPress ENTER to return:')
		return input()
