import pandas as pd
import sqlite3
import os

csv_file = 'raw_data_csv_converted/homicidios.csv'
sqlite_db = 'data_base/tp2.db'

if not os.path.exists(sqlite_db): 
    print(f"Criando o banco de dados {sqlite_db}")
    conn = sqlite3.connect(sqlite_db)
    conn.close()

conn = sqlite3.connect(sqlite_db)


df = pd.read_csv(csv_file, delimiter=',', low_memory=False)

df.replace('--', None, inplace=True)

df.to_sql('homicidios', conn, if_exists='replace', index=False)

conn.close()
