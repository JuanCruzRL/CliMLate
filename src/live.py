import requests
import pandas as pd
import joblib
from data import add_features, OTHER_CITIES

VARIABLES = (
    "temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,"
    "precipitation,weather_code,pressure_msl,surface_pressure,cloud_cover,"
    "vapour_pressure_deficit,wind_speed_10m,wind_direction_10m,wind_gusts_10m,"
    "is_day,shortwave_radiation"
)

COORDS = {
    "Buenos Aires": (-34.61, -58.38), "Santa Rosa": (-36.62, -64.29),
    "Neuquén": (-38.95, -68.06), "Mendoza": (-32.89, -68.84),
    "Córdoba": (-31.42, -64.19), "Santa Fe": (-31.63, -60.70),
    "San Luis": (-33.30, -66.34), "Viedma": (-40.81, -62.99),
    "Corrientes": (-27.47, -58.83), "Formosa": (-26.18, -58.17),
    "Resistencia": (-27.45, -58.99), "San Salvador de Jujuy": (-24.19, -65.30),
    "La Rioja": (-29.41, -66.85), "Posadas": (-27.37, -55.90),
    "Salta": (-24.79, -65.41), "San Juan": (-31.54, -68.54),
    "Río Gallegos": (-51.62, -69.22), "Santiago del Estero": (-27.80, -64.26),
    "Paraná": (-31.73, -60.52), "San Fernando del Valle de Catamarca": (-28.47, -65.79),
    "Rawson": (-43.30, -65.10), "San Miguel de Tucumán": (-26.82, -65.22),
    "Ushuaia": (-54.80, -68.30),
}

def get_city(city):
    lat, lon = COORDS[city]
    res = requests.get(url="https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly={VARIABLES}"
        "&past_hours=6&forecast_hours=1"
        "&timezone=America/Argentina/Buenos_Aires")
    return pd.DataFrame(res.json()["hourly"])

def get_live_data(city):
    df = get_city(city)
    for c in OTHER_CITIES:
        if c == city:
            continue
        other_df = get_city(c)
        other_df.drop(columns=["time"], inplace=True)
        other_df = other_df.add_prefix(f"{c}_")
        df = pd.concat([df, other_df], axis=1)
    df = df.copy()
    df = add_features(df)
    return df.tail(1)

def predict(city):
    row = get_live_data(city)
    model = joblib.load(f"../models/{city}.pkl")
    X = row.drop(columns=["time"])
    return model.predict(X)

print(predict("Buenos Aires"))