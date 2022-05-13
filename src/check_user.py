from dataBase.execute_query import execute_query

def check_username(userid, db_name, query):
    id = execute_query(db_name, query)
    return id