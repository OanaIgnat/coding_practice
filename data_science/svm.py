import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

plt.rcParams['figure.figsize'] = (20.0, 10.0)

'''
How is SVM’s hyperplane different from linear classifiers?

Motivation: Maximize margin: we want to find the classifier whose decision boundary is furthest away from any data point.
We can express the separating hyper-plane in terms of the data points that are closest to the boundary.
And these points are called support vectors.
https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
'''


def read_data():
    # Reading Data
    data = pd.read_csv('data_science/linear_regression/headbrain.csv')
    data.head()

    # Collecting X and Y

    # features
    X1 = data['Head Size(cm^3)'].values
    X2 = data['Brain Weight(grams)'].values
    X = data.drop(['Gender', 'Age Range'], axis=1).values
    # class
    Y = data['Gender'].values - 2

    x1_fem = X1[:50]
    x2_fem = X2[:50]
    x1_male = X1[-50:]
    x2_male = X2[-50:]
    plt.figure(figsize=(8, 6))
    plt.scatter(x1_fem, x2_fem, marker='+', color='green')
    plt.scatter(x1_male, x2_male, marker='_', color='red')
    plt.show()

    return X, Y


def main():
    X, Y = read_data()
    X, Y = shuffle(X, Y)  # need to implement myself
    x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.9)

    X = x_train
    Y = y_train
    epochs = 1
    learning_rate = 0.0001
    n = len(X)
    w1 = np.zeros(n)
    w2 = np.zeros(n)

    X1 = X[:, 0]
    X2 = X[:, 1]


    # Hinge loss
    while epochs < 1000:
        pred = w1 * X1 + w2 * X2
        prod = pred * Y

        regularizer = 1 / epochs  # regularizer decreases while epoch increases
        count = 0
        for val in prod:
            if val > 0:
                w1 = w1 - learning_rate * (2 * regularizer * w1)
                w2 = w2 - learning_rate * (2 * regularizer * w2)
            else:
                w1 = w1 - learning_rate * (2 * regularizer * w1 - X1[count] * Y[count])
                w2 = w2 - learning_rate * (2 * regularizer * w2 - X2[count] * Y[count])
            count += 1

        epochs += 1



    ## Extract the test data features
    test_f1 = x_test[:, 0]
    test_f2 = x_test[:, 1]

    ## Clip the weights
    index = list(range(10, 90))
    w1 = np.delete(w1, index)
    w2 = np.delete(w2, index)

    ## Predict
    y_pred = w1 * test_f1 + w2 * test_f2
    predictions = []
    for val in y_pred:
        if val > 1:
            predictions.append(1)
        else:
            predictions.append(-1)

    print(accuracy_score(y_test, predictions))


if __name__ == "__main__":
    main()
