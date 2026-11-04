from data import prepare_data
from sklearn.metrics import root_mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import HistGradientBoostingRegressor

X_train, X_test, y_train, y_test = prepare_data("Buenos Aires")

model = LinearRegression()
model2 = HistGradientBoostingRegressor()
model.fit(X_train, y_train)
model2.fit(X_train, y_train)
prediction = model.predict(X_test)
prediction2 = model2.predict(X_test)
print(root_mean_squared_error(y_test, prediction))
print(root_mean_squared_error(y_test, prediction2))