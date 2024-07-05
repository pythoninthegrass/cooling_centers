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
csv_file = csv_dir / 'cooling_centers_2024.csv'


def get_lat_long(address):
    geolocator = GoogleV3(api_key=google_api_key)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)
    try:
        location = geocode(address)
        if location:
            lat, lon = location.latitude, location.longitude
            return f"{lat}, {lon}"
        return None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error geocoding {address}: {e}")
        return None


def main():
    # read existing csv
    df = pd.read_csv(csv_file, header=0)

    # find latitude and longitude for each address
    df['latitude_longitude'] = df.apply(lambda row: get_lat_long(f"{row['city_county']}, {row['address']}"), axis=1)

    print(df.head(10))

    # export to csv
    df.to_csv(csv_file, index=False)


if __name__ == '__main__':
    main()
