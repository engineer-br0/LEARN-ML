from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
from matplotlib import pyplot as plt

dbts = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
#print(dbts.keys())
x_train = dbts.data[:-30, 0:9]
y_train = dbts.data[:-30, 9:10]

x_test = dbts.data[-30:, 0:9]
y_test = dbts.data[-30:, 9:10]
#print(y_test)
model = linear_model.LinearRegression()

model.fit(x_train, y_train)
predicted = model.predict(x_test)

print(predicted)
print(mean_squared_error(y_test, predicted))

# plt.scatter(x_test, y_test)
# plt.plot(x_test, predicted)
# plt.show()
#print(dbts.target)
 