#!/usr/bin/env python

import tempfile
import httpx
import rich.progress
from pathlib import Path

url = 'https://www.oge.com/wps/wcm/connect/5fff4221-6696-4166-9129-f431fc5a424f/OGE-Website+updates+2024-Cool+Zones-v2.pdf?MOD=AJPERES&CVID=p0Yt3kc'
dl_dir = Path('../static')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0'
}

with tempfile.NamedTemporaryFile() as dl_file:
    with httpx.stream('GET', url, headers=headers) as response:
        total_length = int(response.headers['Content-Length'])
        with rich.progress.Progress(
            "[progress.percentage]{task.percentage:>3.0f}%",
            rich.progress.BarColumn(bar_width=None),
            rich.progress.DownloadColumn(),
            rich.progress.TransferSpeedColumn(),
        ) as progress:
            download_task = progress.add_task("Download", total=total_length)
            for chunk in response.iter_bytes():
                dl_file.write(chunk)
                progress.update(download_task, completed=response.num_bytes_downloaded)
    dl_file.seek(0)
    with open(f"{dl_dir}/oge_cooling_centers.pdf", 'wb') as f:
        f.write(dl_file.read())
