from data import prepare_data, OTHER_CITIES
from sklearn.metrics import root_mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import HistGradientBoostingRegressor
import joblib
from pathlib import Path

Path("../models").mkdir(exist_ok=True)
city = "Buenos Aires"

X_train, X_test, y_train, y_test = prepare_data(city, OTHER_CITIES)

model = LinearRegression()
model2 = HistGradientBoostingRegressor(
    learning_rate=0.03,
    max_iter=1000,
    max_leaf_nodes=100,
    min_samples_leaf=75,
    random_state=42
)
model.fit(X_train, y_train)
model2.fit(X_train, y_train)
prediction = model.predict(X_test)
prediction2 = model2.predict(X_test)
print(root_mean_squared_error(y_test, prediction))
print(root_mean_squared_error(y_test, prediction2))
joblib.dump(model2, f"../models/{city}.pkl")