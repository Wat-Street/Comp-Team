def query(sql_stmt, cursor):
    cursor.execute(sql_stmt)
    return cursor.fetchall()
