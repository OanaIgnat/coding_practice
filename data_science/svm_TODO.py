'''
How is SVM’s hyperplane different from linear classifiers?

Motivation: Maximize margin: we want to find the classifier whose decision boundary is furthest away from any data point.
We can express the separating hyper-plane in terms of the data points that are closest to the boundary.
And these points are called support vectors.
'''
from random import shuffle

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)


def compute_cost(w, x, y, reg_strength):
    """
    calculate hinge loss
    y_pred = a x + b
    cost function: max(0, 1- y_pred * y)
    """
    n = x.shape[0]
    distances = 1 - y * (np.dot(x, w))
    distances[distances < 0] = 0  # equivalent to max(0, distance)
    hinge_loss = reg_strength * (np.sum(distances) / n)

    # calculate cost
    cost = 1 / 2 * np.dot(w, w) + hinge_loss
    return cost


def calculate_cost_gradient(W, X_batch, Y_batch, reg_strength):
    # if only one example is passed (eg. in case of SGD)
    if type(Y_batch) == np.float64:
        Y_batch = np.array([Y_batch])
        X_batch = np.array([X_batch])  # gives multidimensional array

    distance = 1 - (Y_batch * np.dot(X_batch, W))
    dw = np.zeros(len(W))

    for ind, d in enumerate(distance):
        if max(0, d) == 0:
            di = W
        else:
            di = W - (reg_strength * Y_batch[ind] * X_batch[ind])
        dw += di

    dw = dw / len(Y_batch)  # average
    return dw


def sgd(features, outputs):
    max_epochs = 5000
    reg_strength = 10000
    learning_rate = 0.000001
    weights = np.zeros(features.shape[1])
    nth = 0
    prev_cost = float("inf")
    cost_threshold = 0.01  # in percent
    # stochastic gradient descent
    for epoch in range(1, max_epochs):
        # shuffle to prevent repeating update cycles
        # X, Y = shuffle(features, outputs)
        X, Y = features, outputs
        for ind, x in enumerate(X):
            ascent = calculate_cost_gradient(weights, x, Y[ind], reg_strength)
            weights = weights - (learning_rate * ascent)

        # convergence check on 2^nth epoch
        if epoch == 2 ** nth or epoch == max_epochs - 1:
            cost = compute_cost(weights, features, outputs, reg_strength)
            print("Epoch is: {} and Cost is: {}".format(epoch, cost))
            # stoppage criterion
            if abs(prev_cost - cost) < cost_threshold * prev_cost:
                return weights
            prev_cost = cost
            nth += 1
    return weights


def compute_svm(reg_data, reg_query):
    reg_data = np.array(reg_data)
    X = np.array(reg_data[:, 0])
    Y = np.array(reg_data[:, 1])

    X = np.expand_dims(X, axis=1)
    reg_query = np.expand_dims(reg_query, axis=1)

    W = sgd(X, Y)
    # # classification
    return np.sign(np.dot(np.array(reg_query), W))


def main():
    # Classification Data
    #
    # Column 0: age
    # Column 1: likes pineapple

    clf_data = [
        [22, 1],
        [23, 1],
        [21, 1],
        [18, 1],
        [19, 1],
        [25, -1],
        [27, -1],
        [29, -1],
        [31, -1],
        [45, -1],
    ]
    # Question:
    # Given the data we have, does a 33 year old like pineapples on their pizza?
    clf_query = [33]
    clf_prediction = compute_svm(clf_data, clf_query)

    if clf_prediction == 0:
        print("No, a %d year old does not like pineapples on their pizza" % clf_query[0])
    else:
        print("Yes, a %d year old likes pineapples on their pizza" % clf_query[0])


if __name__ == '__main__':
    main()
