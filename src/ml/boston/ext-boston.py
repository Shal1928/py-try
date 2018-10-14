from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
from mglearn.datasets import load_extended_boston
import matplotlib.pyplot as plt
X, y = load_extended_boston()
print("Форма массива X: {}".format(X.shape))
