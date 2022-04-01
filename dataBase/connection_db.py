import sqlite3

def create_connection(db_name):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        print("База данных создана и успешна подключена")

        stmt = "select sqlite_version();"
        cursor.execute(stmt)
        version = cursor.fetchall()
        print("Версия базы лданных SQLite: ", version)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении SQLite: ", error)
    finally:
        if (connection):
            connection.close()
            print("Соединение с SQLite закрыто")
