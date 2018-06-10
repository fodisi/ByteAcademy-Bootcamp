#!/usr/bin/env python3


from abc import ABC, abstractmethod
import sqlite3 as db


"""Represents a base DAL (Data Access Layer) object."""
class BaseDAL(ABC):
	DB_NAME = "bankapp.db"

	@abstractmethod
	def prepare_insert(self, obj):
		pass

	@abstractmethod
	def prepare_update(self, obj):
		pass

	@abstractmethod
	def prepare_delete(self, obj):
		pass

	@abstractmethod
	def prepare_select(self, id_):
		pass

	@abstractmethod
	def prepare_select_all(self):
		pass
	
	@abstractmethod
	def to_object(self, row):
		pass


	def __execute_non_query(self, sql_command):
		# create a connection to the database
		with db.connect(self.DB_NAME, check_same_thread=False) as conn:
			cursor = conn.cursor()
			#executes and commits the sql command
			cursor.execute(sql_command)
			conn.commit()
			cursor.close()
	
	
	def __execute_query(self, sql_command):
		# create a connection to the database
		with db.connect(self.DB_NAME, check_same_thread=False) as conn:
			cursor = conn.cursor()
			#executes sql command and returns fetched data
			cursor.execute(sql_command)
			return cursor.fetchall()
	

	def insert(self, obj):
		sql_command = self.prepare_insert(obj)
		self.__execute_non_query(sql_command)

	def update(self, obj):
		sql_command = self.prepare_update(obj)
		self.__execute_non_query(sql_command)

	def delete(self, obj):
		sql_command = self.prepare_delete(obj)
		self.__execute_non_query(sql_command)

	def select(self, id_):
		#gets the sql command from the inherited class
		sql_command = self.prepare_select(id_)
		#executes the command and fetches into result
		result = self.__execute_query(sql_command)
		#result receives a list of rows. Need the first row.
		if len(result) > 0:
			return self.to_object(result[0])
		else:
			return None

	def select_all(self):
		sql_command = self.prepare_select_all()
		return self.to_list(self.__execute_query(sql_command))

	def to_list(self, rows):
		objects = []
		for row in rows:
			obj = self.to_object(row)
			if obj != None:
				objects.append(obj)
		
		return objects;
