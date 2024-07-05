#!/usr/bin/env python

import folium
import pandas
from decouple import config
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
csv_dir = base_dir / 'csv'
file_name = config('CSV_FILE', default='cooling_centers_2024.csv')
csv_file = csv_dir / file_name
template_dir = base_dir / 'docs'

df = pandas.read_csv(csv_file, header=0)

m = folium.Map(location=[35.4823241,-97.7593895], zoom_start=7)

for city_county, location_name, address, phone, hours, latlon in zip(df['city_county'], df['location_name'], df['address'], df['phone'], df['hours_of_operation'], df['latitude_longitude']):
    latlon = latlon.strip('"')
    lat, lon = latlon.strip('()').split(',')
    latF = float(lat)
    lonF = float(lon)
    folium.Marker([latF, lonF], popup=f'<div><p>{location_name}</p><p>{address}</p><p>{phone}</p><p>{hours}</p></div>', tooltip=location_name).add_to(m)

m.save(template_dir / 'index.html')
