#!/usr/bin/env python

import hishel
import httpx
import sqlite3
from decouple import config
from pathlib import Path

url = config('URL', default='https://apps.health.ny.gov/statistics/environmental/public_health_tracking/tracker/#/CCList')

filename = Path('../static/ny_cooling_centers.html')
if not filename.exists():
    filename.touch()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0'
}

controller = hishel.Controller(
    cacheable_methods=['GET'],
    cacheable_status_codes=[200],
    allow_stale=True,
    always_revalidate=True,
)

conn = sqlite3.connect('../cache.db')
storage = hishel.SQLiteStorage(connection=conn, ttl=3600)

with httpx.Client() as client:
    with httpx.HTTPTransport() as transport:
        with hishel.CacheTransport(transport, controller=controller, storage=storage) as cache_transport:
            client._transport = cache_transport             # Set cache transport as client's transport
            response = client.get(url, headers=headers)     # Use the client to make the request
            response.raise_for_status()                     # Check for HTTP errors
            print(response.content)

