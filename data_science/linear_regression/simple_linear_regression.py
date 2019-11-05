import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)


def read_data():
    # Reading Data
    data = pd.read_csv('data_science/linear_regression/headbrain.csv')
    print(data.shape)
    data.head()

    # Collecting X and Y
    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values
    return X, Y


def calculate_coefficients(X, Y):
    # Mean X and Y
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    # Total number of values
    m = len(X)

    # Using the formula to calculate b1 and b2
    numer = 0
    denom = 0
    for i in range(m):
        numer += (X[i] - mean_x) * (Y[i] - mean_y)
        denom += (X[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)

    # Print coefficients
    return b0, b1


def plot_results(X, Y, b0, b1):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100

    # Calculating line values x and y
    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x

    # Ploting Line
    plt.plot(x, y, color='#58b970', label='Regression Line')
    # Ploting Scatter Points
    plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

    plt.xlabel('Head Size in cm3')
    plt.ylabel('Brain Weight in grams')
    plt.legend()
    plt.show()

def calculate_error(X, Y, b0, b1):
    # Calculating Root Mean Squares Error
    rmse = 0
    for i in range(len(X)):
        y_pred = b0 + b1 * X[i]
        rmse += (Y[i] - y_pred) ** 2
    rmse = np.sqrt(rmse / len(X))
    print(rmse)

def main():
    X, Y = read_data()
    b0, b1 = calculate_coefficients(X, Y)
    # Ordinary Least Square Method
    calculate_error(X, Y, b0, b1)
    # plot_results(X, Y, b0, b1)

if __name__ == "__main__":
    main()