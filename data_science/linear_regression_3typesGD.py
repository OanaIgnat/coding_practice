import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

'''
If results are not okay (nan or inf -> check learning rate
'''


def compute_linear_regression(reg_data, reg_query, typeGD):
    '''
    y_pred = a x + b
    cost function: 1/n (sum[(y - y_pred) ^ 2]) - MSE
    '''
    reg_data = np.array(reg_data)
    X = np.array(reg_data[:, 0])
    Y = np.array(reg_data[:, 1])
    # plt.scatter(X, Y)
    # plt.show()
    n = len(X)
    l_r = 0.00001
    a, b = 0, 0
    # batch GD
    if typeGD == "Batch":
        for epoch in range(1000):  # calculate cost and update weights
            Y_pred = a * X + b

            deriv_a = (-2 / n) * sum(X * (Y - Y_pred))  # deriv_a = (-2 / n) * np.dot(X, (Y - Y_pred)) # or deriv_a = (-2 / n) * np.matmul(X.T, (Y - Y_pred))
            deriv_b = (-2 / n) * sum(Y - Y_pred)

            a = a - l_r * deriv_a
            b = b - l_r * deriv_b
            # MSE = 1 / n * sum((Y - Y_pred) ** 2) # error/ loss function
            # if epoch % 100:
            #     print(MSE)
    elif typeGD == "SGD":
        # SGD
        for epoch in range(1000):
            a_cost, b_cost = 0, 0
            # todo shuffle X
            for i in range(n):  # update weights
                Y_pred = a * X[i] + b
                for j in range(n):  # calculate cost
                    deriv_a = -2 * X[j] * (Y[j] - Y_pred)
                    deriv_b = -2 * (Y[j] - Y_pred)

                    a_cost += deriv_a
                    b_cost += deriv_b

                a = a - l_r * a_cost
                b = b - l_r * b_cost
            # MSE = sum((Y - Y_pred) ** 2)  # error/ loss function
            # if epoch % 100:
            #     print(MSE)

    elif typeGD == "MiniBatch":
        batch_size = 32
        for epoch in range(1000):
            # todo shuffle X
            for i in range(0, n, batch_size):  # calculate cost & update weights
                X = X[i:i + batch_size]
                Y = Y[i:i + batch_size]
                Y_pred = a * X + b

                deriv_a = (-2 / n) * sum(X * (Y - Y_pred))
                deriv_b = (-2 / n) * sum(Y - Y_pred)

                a = a - l_r * deriv_a
                b = b - l_r * deriv_b
                # MSE = sum((Y - Y_pred) ** 2)  # error/ loss function
                # if epoch % 100:
                #     print(MSE)

    reg_prediction = a * np.array([reg_query]) + b
    return reg_prediction[0]


def main():
    '''
    # Regression Data
    #
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''
    reg_data = [
        [65.75, 112.99],
        [71.52, 136.49],
        [69.40, 153.03],
        [68.22, 142.34],
        [67.79, 144.30],
        [68.70, 123.30],
        [69.80, 141.49],
        [70.01, 136.46],
        [67.90, 112.37],
        [66.49, 127.45],
    ]

    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = 60
    type_GD = ["Batch", "MiniBatch", "SGD"]
    for type in type_GD:
        print("For " + type + " :")
        reg_prediction = compute_linear_regression(reg_data, reg_query, type)
        print("if they are %d inches tall, their weigth is probably %.3f" % (reg_query, reg_prediction))


if __name__ == '__main__':
    main()
