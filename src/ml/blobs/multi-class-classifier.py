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
X, y = make_blobs(random_state=42)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
line = np.linspace(-15, 15)
print("X[:, 0] = {}".format(X[:, 0]))
print("X[:, 01] = {}".format(X[:, 1]))
linear_svm = LinearSVC().fit(X, y)
print("Форма коэф.: {}".format(linear_svm.coef_.shape))
print("Форма конст.: {}".format(linear_svm.intercept_.shape))
mglearn.plots.plot_2d_classification(linear_svm, X, fill=True, alpha=.7)
for coef, intercept, color in zip(linear_svm.coef_, linear_svm.intercept_, ["b", "r", "g"]):
    plt.plot(line, -(line * coef[0] + intercept) / coef[1], c=color)
    plt.ylim(-10, 15)
    plt.xlim(-10, 8)
    plt.xlabel("Признак 0")
    plt.ylabel("Признак 1")
    plt.legend(["Класс 0", "Класс 1", "Класс 2", "Линия класса 0", "Линия класса 1", "Линия класса 2"], loc=(1.01, 0.3))
plt.show()

