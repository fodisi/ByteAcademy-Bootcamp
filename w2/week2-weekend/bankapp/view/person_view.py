#!/usr/bin/env python3


from view.base_view import BaseView
from model.person import Person


class PersonView(BaseView):
	
	def create_person(self, role):
		self.clear()
		data = []
		
		print(34 * '#')
		
		title = 'CREATE NEW {0}:'.format(role.upper())
		print('# {0:^30} #'.format(title))
		print(34 * '#')
		print()
		print('Type the name:')
		data.append(input())
		print('Type the email:')
		data.append(input())
		print('Type the login:')
		data.append(input())
		print('Type the password:')
		data.append(input())
		
		return data

	def view_people(self, people, role):
		self.clear()
		print(80 * '#')
		title = '{0} LIST:'.format(role.upper())
		print('# {0:^76} #'.format(title))
		print(80 * '#')
		print('# {0:<76} #'.format(''))
		print('# {0:<7} | {1:<20} | {2:<20} | {3:<20} #'.format(
				'Id', 
				'Name',
				'Email',
				'Login'
				))
		for person in people:
			print('# {0:07d} | {1:<20} | {2:<20} | {3:<20} #'.format(
				person.id, 
				person.name,
				person.email,
				person.login
				))
		
		print('# {0:<76} #'.format(''))
		print(80 * '#')
		print('\n\nPress ENTER to return:')
		return input()
