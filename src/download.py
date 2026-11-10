import time
from pathlib import Path

import pandas as pd
import requests

from live import COORDS, VARIABLES

RES = Path("../res")
RES.mkdir(exist_ok=True)

for city, (lat, lon) in COORDS.items():
    path = RES / f"{city}.csv"
    if path.is_file():
        print(f"{city}: ya estaba")
        continue

    url = ("https://archive-api.open-meteo.com/v1/archive"
           f"?latitude={lat}&longitude={lon}"
           "&start_date=2010-01-01&end_date=2026-07-31"
           f"&hourly={VARIABLES}"
           "&timezone=America/Argentina/Buenos_Aires")

    while True:
        res = requests.get(url, timeout=120)
        if res.status_code == 429:
            print(f"{city}: limite de la API, 60s de timeout")
            time.sleep(60)
            continue
        res.raise_for_status()
        break

    pd.DataFrame(res.json()["hourly"]).to_csv(path, index=False)
    print(f"{city}: listo")
    time.sleep(10)