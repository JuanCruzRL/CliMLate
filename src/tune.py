from data import prepare_data, OTHER_CITIES
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import RandomizedSearchCV, TimeSeriesSplit

X_train, X_test, y_train, y_test = prepare_data("Buenos Aires", OTHER_CITIES)

model = HistGradientBoostingRegressor()

params = {
    "learning_rate": [0.03, 0.05, 0.1, 0.2],
    "max_iter": [150, 300, 500, 1000],
    "max_leaf_nodes": [15, 31, 40, 63, 100],
    "min_samples_leaf": [20, 50, 75, 100],
}

search = RandomizedSearchCV(model, params, n_iter=10, cv=TimeSeriesSplit(n_splits=3), scoring="neg_root_mean_squared_error", random_state=42)
search.fit(X_train, y_train)
print(search.best_params_)
print(search.best_score_)