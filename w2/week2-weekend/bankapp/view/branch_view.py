#!/usr/bin/env python3


from view.base_view import BaseView
from model.branch import Branch


class BranchView(BaseView):
	
	def create_branch(self):
		self.clear()
		
		print(34 * '#')
		print('# {0:<30} #'.format('Create new branch:'))
		print(34 * '#')
		print()
		print('Type the branch name:')
		return input()

	def view_branches(self, branches):
		self.clear()
		print(44 * '#')
		print('# {0:<40} #'.format('List of Branches:'))
		print(44 * '#')
		print('# {0:<40} #'.format(''))
		print('# {0:<7} | {1:<31}#'.format('Id', 'Name'))
		for branch in branches:
			print('# {0:07d} | {1:<31}#'.format(branch.id, branch.name))
		
		print('# {0:<40} #'.format(''))
		print(44 * '#')
		print('\n\nPress ENTER to return:')
		return input()
