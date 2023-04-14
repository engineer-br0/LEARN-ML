from sklearn import datasets, linear_model, neighbors
from sklearn.metrics import mean_squared_error

iris = datasets.load_iris()
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
# ['setosa' 'versicolor' 'virginica']
print(iris.data.shape)

# model = linear_model.LinearRegression()
model = neighbors.KNeighborsClassifier()
x_train = iris.data[:-10, :]
y_train = iris.target[:-10]

x_test = iris.data[-10: , :]
y_test = iris.target[-10:]

model.fit(x_train, y_train)

predict = model.predict(x_test)

print("predict :" , predict)
print("test : " , y_test)

print("mean error: ", mean_squared_error(y_test, predict))
