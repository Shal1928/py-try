from sklearn.datasets import load_iris
from mglearn.datasets import load_extended_boston
from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from pandas import np
import matplotlib.pyplot as plt
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
ridge1 = Ridge(alpha=1).fit(X_train, y_train)
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
lr = LinearRegression().fit(X_train, y_train)
print("lr.coef_: {}".format(ridge01.coef_))
print("lr.intercept_: {}".format(ridge01.intercept_))
print("Правильность на обучающем наборе: {:.2f}".format(ridge01.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.2f}".format(ridge01.score(X_test, y_test)))
plt.plot(ridge1.coef_, 's', label="Ридж регрессия alpha=1")
plt.plot(ridge10.coef_, 's', label="Ридж регрессия alpha=10")
plt.plot(ridge01.coef_, 's', label="Ридж регрессия alpha=0.1")
plt.plot(ridge01.coef_, 's', label="Ридж регрессия alpha=0.1")
plt.plot(lr.coef_, 'o', label="Линейная регрессия")

plt.xlabel('Индекс коэф.')
plt.ylabel('Оценка коэф.')
plt.hlines(0, 0, len(lr.coef_))
plt.ylim(-25, 25)
plt.legend()
plt.show()
