#!/usr/bin/env python3


from view.account_view import AccountView
from dal.client_accountDAL import ClientAccountDAL
from dal.accountDAL import AccountDAL
from model.client import Client
from model.account import Account

class AccountController():
	def __init__(self):
		self.view = AccountView()

	def __to_client_object(self, data):
		return Client(name=data['name'], 
				      email=data['email'], 
					  login=data['login'], 
					  password=data['password'])


	def __to_account_object(self, data):
		return Account(number=data['number'], 
					   branch_id=data['branch_id'])


	def create_account(self):
		try:
			data = self.view.create_account()
			account = self.__to_account_object(data)
			client = self.__to_client_object(data)
			account_dal = AccountDAL()
			client_dal = ClientAccountDAL()

			try:
				# inserts account into DB
				account_dal.insert(account)
				#Inserts client into DB
				client_dal.insert(client)
				# Gets client from DB to refresh its ID info
				client = client_dal.select_by_login(client.login)
				# Inserts client account into DB
				client_dal.insert_client_account(client, account)
			except Exception:
				# Rollback if any insert command went wrong.
				client_dal.delete_client_account(client, account)
				client_dal.delete(client)
				account_dal.delete(account)
				raise
			
			message = 'Branch|Account: "{0}|{1}" for client "{2}" for  inserted successfully.'
			self.view.show_message('Success', 
									message.format(
										account.number, 
										account.branch_id, 
										client.name), 
									True
								  )
		except Exception as e:
			main_message = 'Error inserting data into database'
			detail_message = 'Check if branch exists or if account number is already in use.'
			self.view.show_message('Error',
								   '{main}\n{detail}\n\n{error}'.format(
										main = main_message,
										detail = detail_message,
										error = e.args[0]),
								   True)

	def list_client_accounts(self):
		try:
			print('create dal')
			dal = ClientAccountDAL()
			print('selecting accoutns')
			accounts = dal.select_all_client_accounts()
			self.view.view_client_accounts(accounts)
		except Exception as e:
			self.view.show_message('Error', e.args[0], True)
