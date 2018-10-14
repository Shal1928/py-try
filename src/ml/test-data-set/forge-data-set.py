from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Класс 0"], ["Класс 1"], loc=4)
plt.xlabel("Перый признак")
plt.ylabel("Второй признак")
print("Форма массива X: {}".format(X.shape))
plt.show()
