#!/usr/bin/env python3

from bankapp.model import Bank
from bankapp.dal import BankDAL

if __name__ == '__main__':
	bank = Bank(1, 'bankname')
	print(bank.name)
	dal = BankDAL(bank)
	dal.print_model()
