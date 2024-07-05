#!/usr/bin/env python

import pdftotree
import pandas as pd
from datetime import datetime
from io import StringIO
from pathlib import Path

# env vars
anno = datetime.now().year
base_dir = Path(__file__).resolve().parents[1]
csv_dir = base_dir / 'csv'
pdf_dir = base_dir / 'static'
pdf_file = pdf_dir / 'oge_cooling_centers.pdf'
csv_file = csv_dir / f"cooling_centers_{anno}.csv"

# TODO: fix 'Maysville/Garvin County'
# ! gets shifted to the left and 'Maysville Public Library' is in the 'city_county' column
# parse pdf into html then into a string
html_content = pdftotree.parse(str(pdf_file))
html_io = StringIO(html_content)
dfs = pd.read_html(html_io)

# combine all dataframes into one
data = []
for df in dfs:
    for index, row in df.iterrows():
        if index == 0:
            continue
        city_county = row[0]
        location_name = row[1]
        address = row[2]
        phone = row[3]
        hours_of_operation = row[4]
        data.append([city_county, location_name, address, phone, hours_of_operation])

df = pd.DataFrame(data, columns=['city_county', 'location_name', 'address', 'phone', 'hours_of_operation'])

# fix double spaces
columns_to_fix = ['city_county', 'location_name', 'address', 'phone', 'hours_of_operation']
for column in columns_to_fix:
    df[column] = df[column].str.replace('  ', ' ')

# fix empty city_county
df['city_county'] = df['city_county'].replace('', float('NaN')).ffill()

# export to csv
df.to_csv(csv_file, index=False)
