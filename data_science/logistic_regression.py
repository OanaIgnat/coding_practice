import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

'''
If results are not okay (nan or inf -> check learning rate

y_pred = w x + b
Loss function: Log Loss -y * log(y_pred) - (1-y) * log(1 - y_pred)
Cost function: 1/n sum(-y * log(y_pred) - (1-y) * log(1 - y_pred))
'''

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def loss(y, y_pred):
    loss = -np.mean(y * (np.log(y_pred)) - (1-y) * np.log(1-y_pred))
    return loss

def compute_logistic_regression(X, y):
    n, nb_features = X.shape[0], X.shape[1]
    l_r = 1e-5
    w, b = np.zeros((nb_features, 1)), 0

    y = y.reshape(n, 1)
    for epoch in range(1000):
        y_pred = sigmoid(np.dot(X, w) + b)

        # dw = 1/n * np.dot(X, (y - y_pred))
        dw = 1/n * np.dot(X.T, (y_pred - y))
        db = 1/n * sum(y_pred - y)

        # update the weights & biases
        w -= l_r * dw
        b -= l_r * db

    return w, b

def predict(X, w, b):
    predictions = sigmoid(np.dot(X, w) + b)
    threshold = 0.5
    return np.array([1 if pred > threshold else 0 for pred in predictions])

def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)

def main():
    '''
           Create data
    '''
    X, y = datasets.make_blobs(
        n_samples=20, n_features=2, centers=2, cluster_std=1.05, random_state=1
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=1)

    '''
        Test Logistic Regression
    '''
    w, b = compute_logistic_regression(X_train, y_train)
    y_pred = predict(X_test, w, b)
    print(accuracy(y_test, y_pred))




if __name__ == '__main__':
    main()

