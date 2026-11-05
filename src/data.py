import pandas as pd
from sklearn.model_selection import train_test_split

OTHER_CITIES = [
    "Santa Rosa", "Neuquén", "Mendoza", "Córdoba", "Santa Fe", "San Luis",
    "Viedma", "Corrientes", "Formosa", "Resistencia", "San Salvador de Jujuy",
    "La Rioja", "Posadas", "Salta", "San Juan", "Río Gallegos",
    "Santiago del Estero", "Paraná", "San Fernando del Valle de Catamarca",
    "Rawson", "San Miguel de Tucumán", "Ushuaia",
]

def prepare_data(city, other_cities):
    df = pd.read_csv(f"../res/{city}.csv")
    for c in other_cities:
        other_df = pd.read_csv(f"../res/{c}.csv")
        other_df.drop(columns=["time"], inplace=True)
        other_df = other_df.add_prefix(f"{c}_")
        df = pd.concat([df, other_df], axis=1)

    df = df.copy()
    df["target"] = df["temperature_2m"].shift(-24)
    df.dropna(subset=["target"], inplace=True)
    df["time"] = pd.to_datetime(df["time"])
    df["hour"] = df["time"].dt.hour
    df["month"] = df["time"].dt.month
    df["temperature_1h"] = df["temperature_2m"].shift(1)
    df["temperature_3h"] = df["temperature_2m"].shift(3)
    df["temperature_6h"] = df["temperature_2m"].shift(6)
    df.dropna(inplace=True)

    X = df.drop(columns=["target", "time"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)
    return X_train, X_test, y_train, y_test