import pandas as pd
data = pd.read_csv(r"C:\Users\hency\OneDrive\Desktop\Internship\day 13\apples_and_oranges - apples_and_oranges.csv")
from sklearn.model_selection import train_test_split
training_set, test_set = train_test_split(data, test_size = 0.2, random_state = 1)
X_train = training_set.iloc[:,0:2].values
Y_train = training_set.iloc[:,2].values
X_test = test_set.iloc[:,0:2].values
Y_test = test_set.iloc[:,2].values
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state = 1)
classifier.fit(X_train,Y_train)
Y_pred = classifier.predict(X_test)
test_set["Predictions"] = Y_pred
Y_test_pred = classifier.predict([[69.0, 4.39]])
print(Y_test_pred)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)
accuracy = float(cm.diagonal().sum())/len(Y_test)
print("\nAccuracy Of SVM For The Given Dataset : ", accuracy)

# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# Y_train = le.fit_transform(Y_train)
# from sklearn.svm import SVC
# classifier = SVC(kernel='rbf', random_state = 1)
# classifier.fit(X_train,Y_train)
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# plt.figure(figsize = (7,7))
# X_set, y_set = X_train, Y_train
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01), np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('black', 'white')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'orange'))(i), label = j)
# plt.title('Apples Vs Oranges')
# plt.xlabel('Weight In Grams')
# plt.ylabel('Size in cm')
# plt.legend()
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# plt.figure(figsize = (7,7))
# X_set, y_set = X_test, Y_test
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),alpha = 0.75, cmap = ListedColormap(('black', 'white')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],c = ListedColormap(('red', 'orange'))(i), label = j)
# plt.title('Apples Vs Oranges Predictions')
# plt.xlabel('Weight In Grams')
# plt.ylabel('Size in cm')
# plt.legend()
# plt.show()