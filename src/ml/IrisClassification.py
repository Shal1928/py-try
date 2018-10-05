from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
# print(iris_dataset['DESCR'][:193] + "\n...")
print("Название сортов: {}".format(iris_dataset['target_names']))
print("Название признаков: {}".format(iris_dataset['feature_names']))
print("Форма массива data: {}".format(iris_dataset['data'].shape))
print("Первые пять строк массива data:\n{}".format(iris_dataset['data'][:5]))
