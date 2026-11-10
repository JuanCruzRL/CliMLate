from live import predict
from db import save_prediction

city = "Buenos Aires"
save_prediction(city, predict(city))