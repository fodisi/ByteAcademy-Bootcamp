#!/usr/bin/env python3

from bankapp.model import Bank, Branch
from bankapp.dal import BankDAL

if __name__ == '__main__':
	bank = Bank(1, 'bankname')
	branch = Branch(1, 'branch1')
	bank.add_branch(branch)
	
	print(bank.name)
	print(branch.name)
	print(len(bank.branches))
	
	print(bank.branch_exists(1))
	print(bank.branch_exists(2))
