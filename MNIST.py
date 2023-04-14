from sklearn import datasets, neighbors
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

mnist = datasets.fetch_openml('mnist_784')
# dict_keys(['data', 'target', 'frame', 'categories', 'feature_names', 'target_names', 'DESCR', 'details', 'url'])
#print(mnist.DESCR)

pic1 = mnist.data.iloc[2000]
pic1 = pic1.values.reshape(28, 28)

plt.imshow(pic1, cmap=matplotlib.cm.binary)

x_train = mnist.data.iloc[:-20, :]
y_train = mnist.target.iloc[:-20]

x_test = mnist.data.iloc[-20:, :]
y_test = mnist.target.iloc[-20:]

# model = neighbors.KNeighborsClassifier()

# model.fit(x_train, y_train)

# pred = model.predict(x_test)

# print("ytest hai : ", y_test)
# print("predicted hai : ", pred)