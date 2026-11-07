# Machine Learning model to predict weather 24h ahead in the city of Buenos Aires

Machine Learning project to predict temperature in 24h based on today's weather.

## Getting data

All data is downloaded from Open-Meteo, ERA5. It has weather features for every hour, from 2010 to 2026. (DOWNLOAD HERE)

## Analyzing the data

As the first step of a ML project, I analyzed the data that the model will be training with. A good start is to check if there is any broken or absent information in the dataframe.
In this case there is no lack of information in any rows of the dataframe as the data's been built by a model. This dataframe has 145344 rows and 16 columns. Temperature ranges from -1.4 to 38.9 °C. It is relevant to say that temperature has a strong daily cycle and tends to follow a trend.

## Baseline

The baseline is used to compare against the future model, it predicts that the temperature tomorrow will be the same as now. First I need to split the data into train and test sets, the data is chronological and the model will predict the future from the past, so the test set must come after the train set. In this case, the baseline had a root mean squared error of 3.015 °C. This means that the baseline's predictions are off by an average 3.015 °C.

## Model

I trained two models on the same data and compared them against the baseline, adding features one step at a time to measure the improvement of the model's predictions. All errors are RMSE on the test set.

| Step | RMSE (°C) |
|---|---|
| Baseline | 3.015 |
| Linear regression | 2.75 |
| Gradient boosting | 2.61 |
| + hour and month | 2.57 |
| + temperature lags | 2.56 |
| + hour, month and temperature lags | 2.44 |
| + Neuquén | 2.07 |
| + the other 21 provincial capitals | 1.93 |
| + tuned hyperparameters | 1.86 |

When adding features from other cities we can see an improvement in the model with the following errors:

## Hiperparameters

I tuned the gradient boosting model with `RandomizedSearchCV` and `TimeSeriesSplit` using the training set. So the test stayed clean for the final measurment.

The best parameters came in to be: `learning_rate=0.03`, `max_iter=1000`, `max_leaf_nodes=100`, `min_samples_leaf=75`