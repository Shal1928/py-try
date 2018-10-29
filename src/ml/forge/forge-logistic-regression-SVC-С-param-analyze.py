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
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from pandas import np
import matplotlib.pyplot as plt
mglearn.plots.plot_linear_svc_regularization()
plt.show()

