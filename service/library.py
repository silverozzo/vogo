from guts.config import Config

import sqlite3


class Library:
	def __init__(self):
		self.conn = sqlite3.connect(Config.library_db)
		self.curs = self.conn.cursor()
		self.curs.execute('create table if not exists tabl ' +
			'(id integer primary key, typer text, name text, code text)')
		self.conn.commit()
	
	def add_tabl(self, typer, name, code, output):
		self.curs.execute('insert into tabl (typer, name, code) values (\'' + 
			typer + '\', \'' + name + '\', \'' + code + '\')')
		self.conn.commit()