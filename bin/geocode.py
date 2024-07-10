#!/usr/bin/env python

import pandas as pd
from decouple import config
from geopy.geocoders import GoogleV3
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from pathlib import Path

# env vars
base_dir = Path(__file__).resolve().parents[1]
google_api_key = config("GOOGLE_API_KEY")
csv_dir = base_dir / 'csv'
filename = config('CSV_FILE', default='ny_cooling_centers_2024.csv')
csv_file = csv_dir / filename

# initialize dataframe
df = None

geolocator = GoogleV3(api_key=google_api_key)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)


def get_lat_long(address):
    try:
        location = geocode(address)
        if location:
            lat, lon = location.latitude, location.longitude
            return f"{lat}, {lon}"
        return None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error geocoding {address}: {e}")
        return None


def set_lat_long(location_column, address_column):
    df['latitude_longitude'] = df.apply(
        lambda row: get_lat_long(f"{row[location_column]}, {row[address_column]}"), axis=1
    )


def get_city_county(coordinates):
    try:
        location = geolocator.reverse(coordinates, exactly_one=True)
        address = location.raw['address_components']
        city = county = None
        for component in address:
            if 'locality' in component['types']:
                city = component['long_name']
            if 'administrative_area_level_2' in component['types']:
                county = component['long_name']
        return f"{city}/{county}" if city and county else None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error reverse geocoding {coordinates}: {e}")
        return None


def set_city_county():
    global df
    if 'latitude_longitude' in df.columns:
        df['city_county'] = df['latitude_longitude'].apply(lambda x: get_city_county(x))
    else:
        print("No 'latitude_longitude' column found in dataframe.")


def main():
    location_column = 'location_name'
    address_column = 'address'
    global df
    df = pd.read_csv(csv_file, header=0)
    if 'latitude_longitude' not in df.columns or df['latitude_longitude'].isnull().all():
        df = set_lat_long(location_column, address_column)
    else:
        print("All rows have 'latitude_longitude' values.")
    if 'city_county' not in df.columns or df['city_county'].isnull().all():
        df = set_city_county(df)
        cols = ['city_county'] + [col for col in df.columns if col != 'city_county']
        df = df[cols]
        df.to_csv(csv_file, index=False)
    else:
        print("All rows have 'city_county' values.")
    print(df.head(10))


if __name__ == '__main__':
    main()
