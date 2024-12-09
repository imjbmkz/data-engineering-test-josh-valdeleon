import sqlite3
import pandas as pd

def load_to_database(df: pd.DataFrame, con: sqlite3.Connection, table_name: str):
    df.to_sql(table_name, con, if_exists="replace", index=False)