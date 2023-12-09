# -*- coding: utf-8 -*-
"""PCAandNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KRR5P01cbXvvIi1zPdsRVB52_lLrGID6

#EXERCISE-11

##PCA AND NEURAL NETWORKS
###SHREYAS SAMPANGI RAMAIAH
###ENG21CS0390
"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
import tensorflow as tf
from keras import layers, models

"""Synthesizing our dataset:"""

X, y = make_classification(n_samples=600, n_features=15, n_classes=2, random_state=42)

"""Test-Train split:"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Standardizing the dataset:"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""Principal Component Analysis:"""

pca = PCA(n_components=10)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

"""Building a neural network:"""

model = models.Sequential([
    layers.Dense(64, activation='relu', input_dim=10),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

"""Training the neural network:"""

model.fit(X_train_pca, y_train, epochs=10, batch_size=32, validation_split=0.2)

"""Model accuracy on test set:"""

y_pred = (model.predict(X_test_pca) > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

"""Building Multi-layer Perceptron classifier:

"""

from sklearn.neural_network import MLPClassifier
mlp_classifier = MLPClassifier(hidden_layer_sizes=(128, 64, 32), max_iter=1000, random_state=42)
mlp_classifier.fit(X_train_pca, y_train)

"""Model Evaluation:"""

y_pred = mlp_classifier.predict(X_test_pca)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')