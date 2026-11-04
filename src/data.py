import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(city):
    df = pd.read_csv(f"../res/{city}.csv")
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