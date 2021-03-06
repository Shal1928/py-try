from sklearn.datasets import load_iris
from sklearn.datasets import make_blobs
from mglearn.datasets import load_extended_boston
from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from pandas import np
import matplotlib.pyplot as plt
X = np.array([[0, 1, 0, 1],
              [1, 0, 1, 1],
              [0, 0, 0, 1],
              [1, 0, 1, 0]])
y = np.array([0, 1, 0, 1])
counts = {}
print(X.shape)
for label in np.unique(y):
    # итерируем по каждому классу
    # подсчитываем элементы 1 по признаку
    print("y = {}".format(y))
    print("label={}".format(label))
    print("y == label -> {}".format(y == label))
    print("X = {}".format(X[y == label]))
    print("sum = {}".format(X[y == label].sum(axis=0)))
    counts[label] = X[y == label].sum(axis=0)
print("Частоты признаков:\n{}".format(counts))
