class Logger:
	_records = []
	
	def clear():
		Logger._records = []
	
	def log(rec):
		Logger._records.append(rec)
	
	def get():
		return Logger._records
