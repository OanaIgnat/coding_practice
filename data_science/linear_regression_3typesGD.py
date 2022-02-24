import numpy as np

'''
If results are not okay (nan or inf -> check learning rate

y_pred = w x + b
Square Loss function: (y - y_pred) ^ 2
Cost function: 1/n sum((y - y_pred) ^ 2)
'''

def compute_linear_regression(X, y, reg_query, typeGD):
    n = len(X)
    l_r = 1e-5
    w, b = 0, 0
    '''
        The weights/params get updated:
        Only after all training data has been evaluated/ 1 epoch
        Pros:
        Cons: 
    '''
    if typeGD == "Batch": # Vanilla
        for epoch in range(1000):  # calculate cost and update weights
            y_pred = w * X + b
            
            dw = (-2 / n) * np.dot(X, (y - y_pred))  # or (-2 / n) * np.matmul(X.T, (y - y_pred)) or (-2 / n) * sum(X * (y - y_pred))
            db = (-2 / n) * sum(y - y_pred)

            # update the weights & biases
            w -= l_r * dw
            b -= l_r * db

    # The weights/params get updated for each data point
    # Pros:
    # Cons:
    elif typeGD == "SGD":
        for epoch in range(1000):
            w_cost, b_cost = 0, 0
            # todo shuffle X
            for i in range(n):  # update weights
                y_pred = w * X[i] + b
                for j in range(n):  # calculate cost
                    dw = -2 * X[j] * (y[j] - y_pred)
                    db = -2 * (y[j] - y_pred)

                    w_cost += dw
                    b_cost += db

                # update the weights
                w -= l_r * w_cost
                b -= l_r * w_cost

    # splits the training data points into small batches and performs an update for each batch
    # Pros: Balances the robustness of SGD with the efficiency of Batch GD
    elif typeGD == "MiniBatch":
        batch_size = 32
        for epoch in range(1000):
            # todo shuffle X
            for i in range(0, n, batch_size):  # calculate cost & update weights
                X = X[i:i + batch_size]
                y = y[i:i + batch_size]
                y_pred = w * X + b

                dw = (-2 / n) * np.dot(X, (y - y_pred))
                db = (-2 / n) * sum(y - y_pred)

                w -= l_r * dw
                b -= l_r * db


    reg_prediction = w * np.array([reg_query]) + b
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

    reg_data = np.array(reg_data)
    X = np.array(reg_data[:, 0])
    y = np.array(reg_data[:, 1])

    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = 60
    type_GD = ["Batch", "MiniBatch", "SGD"]
    for type in type_GD:
        print("For " + type + " :")
        reg_prediction = compute_linear_regression(X, y, reg_query, type)
        print("if they are %d inches tall, their weigth is probably %.3f" % (reg_query, reg_prediction))


if __name__ == '__main__':
    main()
