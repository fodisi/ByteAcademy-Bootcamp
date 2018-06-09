#!/usr/bin/env python3


from bankapp.model import Bank, Branch, Account
from bankapp.dal import BankDAL


if __name__ == '__main__':
	bank = Bank(1, 'bankname')
	branch = Branch(1, 'branch1')
	
	bank.add_branch(branch)
	print('bank name' + bank.name)
	print('branch name' + branch.name)
	print('branches count {0}'.format(len(bank.branches)))
	
	print('branch {0} exists? {1}'.format(1, bank.branch_exists(1)))
	print('branch {0} exists? {1}'.format(2, bank.branch_exists(2)))

	account = Account(1234)
	
	account.deposit(1, '2018-06-09', 'd1', 1000)
	account.deposit(1, '2018-06-09', 'd1', 500)
	
	account.withdrawal(1, '2018-06-09', 'd1', 100)
	
	branch.create_account(account)
	
	print('account balance: {0}'.format(account.get_balance()))
	
	
