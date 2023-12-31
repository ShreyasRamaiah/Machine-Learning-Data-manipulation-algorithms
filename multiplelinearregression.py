# -*- coding: utf-8 -*-
"""Multiplelinearregression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XmTVop86AaBg3m2CUrYFX84N7YINJjqA

Excercise-2 Multiple Linear Regression
Shreyas Sampangi Ramaiah
ENG21CS0390
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cardf = pd.read_csv('/content/carprice_multregression.csv')
cardf

from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(cardf, test_size = 0.3, random_state = 42)

features = list(cardf.columns)
features.remove('price')

X_train = train_df[features]
y_train = train_df['price']
X_test = test_df[features]
y_test = test_df['price']

def standard_norm(series):
  series_mean = series.mean()
  series_std = series.std()
  new_series = (series - series_mean) / series_std
  return new_series

X_train[X_train.columns[:16]] = X_train[X_train.columns[:16]].apply(standard_norm, axis = 0)
X_test[X_test.columns[:16]] = X_test[X_test.columns[:16]].apply(standard_norm, axis = 0)


major_features = {}
for f in features:
  corr_coef = np.corrcoef(cardf['price'], cardf[f])[0, 1]
  if (corr_coef >= 0.5) or (corr_coef <= -0.5):
    major_features[f] = corr_coef


print("Number of features moderately to highly correlated with price =", len(major_features), "\n")
major_features

from sklearn.linear_model import LinearRegression
sk_lin_reg_final = LinearRegression().fit(X_train, y_train)
y_train_pred = sk_lin_reg_final.predict(X_train)
y_train_pred[:10]

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error
print("Train set")
print('-' * 50)

train_r2_score = r2_score(y_train, y_train_pred)
train_adj_r2_score = 1 - (1 - train_r2_score) * (X_train.shape[0] - 1)/(X_train.shape[0] - X_train.shape[1] - 1)

print(f"R-squared = {train_r2_score:.3f}")
print(f"Adjusted R-squared = {train_adj_r2_score:.3f}")
print(f"Mean absolute error = {mean_absolute_error(y_train, y_train_pred):.3f}")
print(f"Mean squared error = {mean_squared_error(y_train, y_train_pred):.3f}")
print(f"Root mean squared error = {np.sqrt(mean_squared_error(y_train, y_train_pred)):.3f}")