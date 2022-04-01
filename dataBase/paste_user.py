from dataBase.execute_query import execute_query
from create_bot import connection


def paste_user(user, connection):
    stmt = "INSERT INTO `users`(`uni`, `department`, `direction`, `subject`, `type_work`, `date`, `status`, `username`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    cursor = connection.cursor()
    cursor.executemany(stmt, user)
    connection.commit()