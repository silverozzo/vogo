from guts.config import Config

import os
import shutil
import sqlite3


class Library:
	def __init__(self):
		self.conn = sqlite3.connect(Config.library_db)
		self.conn.row_factory = sqlite3.Row
		self.curs = self.conn.cursor()
		self.curs.execute('create table if not exists tabl ' +
			'(id integer primary key, typer text, name text, code text)')
		self.conn.commit()
	
	def add_tabl(self, typer, name, code, output):
		self.del_tabl(name)
		if (len(code) == 0):
			return
		self.curs.execute('insert into tabl (typer, name, code) values ' + 
			'(?, ?, ?)', (typer, name, code))
		self.conn.commit()
		shutil.copyfile('output/' + output + '.png', 
			'library/' + name + '.png')
	
	def del_tabl(self, name):
		self.curs.execute('delete from tabl where name=?', [name])
		self.conn.commit()
		path = 'library/' + name + '.png'
		if os.access(path, os.F_OK):
			os.remove(path)
	
	def get_tabls(self):
		result = []
		for row in self.curs.execute('select * from tabl'):
			result.append(row)
		return result