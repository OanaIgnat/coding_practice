'''
Multiple Linear Regression is a type of Linear Regression when the input has multiple features(variables).
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)
from mpl_toolkits.mplot3d import Axes3D


def read_data():
    data = pd.read_csv('data_science/linear_regression/student.csv')
    math = data['Math'].values
    read = data['Reading'].values
    write = data['Writing'].values
    # # Ploting the scores as scatter plot
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.scatter(math, read, write, color='#ef1234')
    # plt.show()
    m = len(math)
    x0 = np.ones(m)
    X = np.array([x0, math, read]).T
    # Initial Coefficients
    B = np.array([0, 0, 0])
    Y = np.array(write)
    alpha = 0.0001
    return X, Y, B, alpha


def cost_function(X, Y, B):
    m = len(Y)
    J = np.sum((np.dot(X, B) - Y) ** 2) / (2 * m)
    return J


def gradient_descent(X, Y, B, alpha, iterations):
    cost_history = [0] * iterations
    m = len(Y)

    for iteration in range(iterations):
        hypothesis = np.dot(X, B)
        loss = hypothesis - Y
        gradient = np.dot(X.T, loss) / m
        B = B - alpha * gradient
        cost = cost_function(X, Y, B)
        cost_history[iteration] = cost
    return B, cost_history


# Model Evaluation - RMSE
def calculate_error(Y, Y_pred):
    # Calculating Root Mean Squares Error
    rmse = np.sqrt(sum((Y - Y_pred) ** 2) / len(Y))
    print(rmse)
    return rmse


def main():
    X, Y, B, alpha = read_data()
    inital_cost = cost_function(X, Y, B)
    print(inital_cost)

    # 100000 Iterations
    newB, cost_history = gradient_descent(X, Y, B, alpha, 100000)
    # New Values of B
    print(newB)
    # Final Cost of new B
    print(cost_history[-1])

    Y_pred = X.dot(newB)
    rmse = calculate_error(Y, Y_pred)


if __name__ == "__main__":
    main()
