import pandas as pd

# util for querying data
def query(sql_query: str, cursor) -> list[str]:
    cursor.execute(sql_query)
    return cursor.fetchall()

def query_df(sql_query: str, table_name: str, cursor) -> list[str]:
    cols = [r[0] for r in query(f"SHOW COLUMNS FROM {table_name}", cursor)]
    df = pd.DataFrame(query(sql_query, cursor))
    df.columns = cols
    return df