import numpy as np
import matplotlib.pyplot as plt
from ipython_genutils.py3compat import xrange


def create_data():
    np.random.seed(12)
    num_observations = 5000

    x1 = np.random.multivariate_normal([0, 0], [[1, .75], [.75, 1]], num_observations)
    x2 = np.random.multivariate_normal([1, 4], [[1, .75], [.75, 1]], num_observations)

    X = np.vstack((x1, x2)).astype(np.float32)
    Y = np.hstack((np.zeros(num_observations),
                   np.ones(num_observations)))
    return X, Y


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def log_likelihood(x, y, w):
    scores = np.dot(x, w)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


def logistic_regression(x, y, num_steps, learning_rate):
    intercept = np.ones((x.shape[0], 1))
    x = np.hstack((intercept, x))

    w = np.zeros(x.shape[1])

    for step in xrange(num_steps):
        scores = np.dot(x, w)
        predictions = sigmoid(scores)

        # Update weights with gradient
        error = y - predictions
        gradient = np.dot(x.T, error)
        w += learning_rate * gradient

        # Print log-likelihood every so often
        if step % 10000 == 0:
            print(log_likelihood(x, y, w))
    return w


def compute_final_score(x, w, y):
    final_scores = np.dot(x, w)
    preds = np.round(sigmoid(final_scores))
    print('Accuracy from scratch: {0}'.format((preds == y).sum().astype(float) / len(preds)))


def main():
    x, y = create_data()
    num_steps, learning_rate = 300000, 5e-5
    w = logistic_regression(x, y, num_steps, learning_rate)
    compute_final_score(x, w, y)


if __name__ == "__main__":
    main()
