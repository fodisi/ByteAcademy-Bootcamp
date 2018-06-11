#!/usr/bin/env python3


from view.base_view import BaseView


class LoginView(BaseView):
	
	def show_login(self):
		
		self.clear()
		login, pwd = '', ''
		
		print(34 * '#')
		print('# {0:^30} #'.format('LOGIN'))
		print(34 * '#')
		print()
		
		print('Type your login:')
		login = input()
		print('Type your password:')
		pwd = input()
		return login, pwd
