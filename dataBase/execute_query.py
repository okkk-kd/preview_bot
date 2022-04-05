import sqlite3

def execute_query(db_name, query):
	try:
		connection = sqlite3.connect(db_name)
		cursor = connection.cursor()
		print("База данных подключена")
		if (query.find(".sql") > 0):
			with open(query, 'r') as sqlite_file:
				sql_script = sqlite_file.read()
			cursor.executescript(sql_script)
			print("Скрипт SQLite успешно выполнен")
			cursor.close()
			return 0
		else:
			cursor.execute(query)
			connection.commit()
			print("Код SQLite успешно выполнен")
			result = cursor.fetchall()
			cursor.close()
			return result

	except sqlite3.Error as error:
		print("Ошибка при подключении", error)
		return 0
	finally:
		if (connection):
			connection.close()
			print("Соединение с базой данных закрыто")

def paste_user(db_name, user):
	stmt = "INSERT INTO `bot`(`name`, `phone`, `tg_id`, `nickname`, `status`, `tariff`) VALUES (?, ?, ?, ?, ?, ?)"
	try:
		connection = sqlite3.connect(db_name)
		cursor = connection.cursor()
		print("База данных подключена")
		cursor.executemany(stmt, user)
		connection.commit() 
		print("RJl1 SQLite успешно выполнен")
	except sqlite3.Error as error:
		print("Ошибка при подключении", error)
	finally:
		if (connection):
			connection.close()
			print("Соединение с базой данных закрыто")
	
			