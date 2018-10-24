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
from sklearn.linear_model import Lasso
from pandas import np
import matplotlib.pyplot as plt
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
lasso = Lasso().fit(X_train, y_train)
lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
print("lr.coef_: {}".format(lasso.coef_))
print("lr.intercept_: {}".format(lasso.intercept_))
print("Правильность на обучающем наборе: {:.2f}".format(lasso.score(X_train, y_train)))
print("Правильность на контрольном наборе: {:.2f}".format(lasso.score(X_test, y_test)))
print("Кол-во исп. признаков: {:.2f}".format(np.sum(lasso.coef_ != 0)))
print("\nalpha=0.1, max_iter=100000:")
print("Правильность на обучающем наборе: {:.2f}".format(lasso001.score(X_train, y_train)))
print("Правильность на контрольном наборе: {:.2f}".format(lasso001.score(X_test, y_test)))
print("Кол-во исп. признаков: {:.2f}".format(np.sum(lasso001.coef_ != 0)))

lasso00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)
print("\nalpha=0.0001, max_iter=100000:")
print("Правильность на обучающем наборе: {:.2f}".format(lasso00001.score(X_train, y_train)))
print("Правильность на контрольном наборе: {:.2f}".format(lasso00001.score(X_test, y_test)))
print("Кол-во исп. признаков: {:.2f}".format(np.sum(lasso00001.coef_ != 0)))

plt.plot(lasso.coef_, 's', label="Ридж регрессия alpha=1")
plt.plot(lasso001.coef_, 's', label="Ридж регрессия alpha=10")
plt.plot(lasso00001.coef_, 's', label="Ридж регрессия alpha=0.1")

ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
lr = LinearRegression().fit(X_train, y_train)
plt.plot(ridge01.coef_, 's', label="Ридж регрессия alpha=0.1")
plt.plot(lr.coef_, 'o', label="Линейная регрессия")

plt.xlabel('Индекс коэф.')
plt.ylabel('Оценка коэф.')
plt.ylim(-25, 25)
plt.legend(ncol=2, loc=(0, 1.05))
plt.show()

