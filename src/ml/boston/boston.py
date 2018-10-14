from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
boston = load_boston()
print("Форма массива data для набора boston: {}".format(boston.data.shape))
