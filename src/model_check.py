import joblib
from data import prepare_data, OTHER_CITIES
from sklearn.metrics import root_mean_squared_error

model = joblib.load("../models/Buenos Aires.pkl")
X_train, X_test, y_train, y_test = prepare_data("Buenos Aires", OTHER_CITIES)
prediction = model.predict(X_test)
print(root_mean_squared_error(y_test, prediction))