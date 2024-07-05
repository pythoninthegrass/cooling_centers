#!/usr/bin/env python

import pandas as pd
import sqlite3
from decouple import config
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
csv_dir = base_dir / 'csv'
file_name = config('CSV_FILE', default='ok_cooling_centers_2024.csv')
csv_file = csv_dir / file_name
db_dir = base_dir / 'db'
db_file = db_dir / 'cooling_centers.db'

db_file.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_file, header=0)

conn = sqlite3.connect(db_file)

df.to_sql('cooling_centers', conn, if_exists='replace', index=False)

print("DB created successfully! The first 5 rows are:\n")
query = "SELECT * FROM cooling_centers LIMIT 5"
result = conn.execute(query)
print('\n'.join(', '.join(str(cell) for cell in row) for row in result))

conn.close()
