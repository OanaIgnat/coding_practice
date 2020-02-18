'''
How is SVM’s hyperplane different from linear classifiers?

Motivation: Maximize margin: we want to find the classifier whose decision boundary is furthest away from any data point.
We can express the separating hyper-plane in terms of the data points that are closest to the boundary.
And these points are called support vectors.
'''

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

'''
If results are not okay (nan or inf -> check learning rate
'''

def compute_svm(reg_data, reg_query):
    '''
    y_pred = a x + b
    cost function: max(0, 1- y_pred * y)
    '''
    reg_data = np.array(reg_data)
    X = np.array(reg_data[:, 0])
    Y = np.array(reg_data[:, 1])
    # plt.scatter(X, Y)
    # plt.show()

    n = len(X)
    l_r = 0.000001
    reg_strength = 1
    a = 0

    for epoch in range(500):
        a_cost = 0
        for i in range(n):
            #todo shuffle X,Y
            Y_pred = a * X[i]
            d = Y[i] * Y_pred
            for j in range(n): #SGD
                if d >= 1:
                    deriv = a
                else:
                    deriv = a - reg_strength * Y[j] * X[j]
                a_cost += deriv
            # todo update weights
            a = a - l_r * a_cost
    # classification
    return np.sign(a * np.array(reg_query))


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
