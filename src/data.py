import pandas as pd
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("../res/Buenos Aires.csv")

df["target"] = df["temperature_2m"].shift(-24)
df.dropna(subset=["target"], inplace=True)

X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

print(root_mean_squared_error(y_test, X_test["temperature_2m"]))