import requests
import pandas as pd
from data import add_features

VARIABLES = (
    "temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,"
    "precipitation,weather_code,pressure_msl,surface_pressure,cloud_cover,"
    "vapour_pressure_deficit,wind_speed_10m,wind_direction_10m,wind_gusts_10m,"
    "is_day,shortwave_radiation"
)

res = requests.get(url="https://api.open-meteo.com/v1/forecast"
    "?latitude=-34.61&longitude=-58.38"
    f"&hourly={VARIABLES}"
    "&past_hours=6&forecast_hours=1"
    "&timezone=America/Argentina/Buenos_Aires")

df = pd.DataFrame(res.json()["hourly"])
df = add_features(df)
df.dropna(inplace=True)
print(df)