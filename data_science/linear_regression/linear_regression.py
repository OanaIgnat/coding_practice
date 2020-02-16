import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)


def read_data():
    # Reading Data
    data = pd.read_csv('data_science/linear_regression/headbrain.csv')
    data.head()

    # Collecting X and Y
    X1 = data['Head Size(cm^3)'].values
    X2 = data['Brain Weight(grams)'].values

    Y = data['Gender'].values

    x1 = X1[:50]
    x2  =X2[-50:]

    plt.scatter(x1, x2)
    # plt.show()

    return X, Y

def main():
    X,Y = read_data()

    n = len(X)
    learning_rate = 0.0001
    nb_epochs = 1000
    # y = ax + b
    a = 0
    b = 0

    for epoch in range(nb_epochs):
        prediction = a * X + b
        error = Y - prediction
        mean_squared_error = sum(error ** 2)
        mean_squared_error = mean_squared_error / n
        a = a - learning_rate * 2 * sum(error * X) / n
        b = b - learning_rate * 2 * sum(error) / n
        if epoch % 10:
            # print("Mean squared error %0.2f" % (mean_squared_error))
    print(a, b)

    # # Building the model
    # m = 0
    # c = 0
    #
    # L = 0.0001  # The learning Rate
    # epochs = 100 # The number of iterations to perform gradient descent
    #
    # n = float(len(X))  # Number of elements in X
    #
    # # Performing Gradient Descent
    # for i in range(epochs):
    #     Y_pred = m * X + c  # The current predicted value of Y
    #     D_m = (-2 / n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    #     D_c = (-2 / n) * sum(Y - Y_pred)  # Derivative wrt c
    #     m = m - L * D_m  # Update m
    #     c = c - L * D_c  # Update c
    #
    # print(m, c)
    #
    # # Making predictions
    # Y_pred = m * X + c
    #
    # plt.scatter(X, Y)
    # plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
    # plt.show()






if __name__ == "__main__":
    main()