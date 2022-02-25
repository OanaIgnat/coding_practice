import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

'''
How is SVM’s hyperplane different from linear classifiers?

Motivation: Maximize margin: we want to find the classifier whose decision boundary is furthest away from any data point.
We can express the separating hyper-plane in terms of the data points that are closest to the boundary.
And these points are called support vectors.
'''

class SVM:

    def __init__(self, lr_hyperparam=1e-3, lambda_hyperparam=1e-2, n_iter=100):
        self.lr_hyperparam = lr_hyperparam
        self.lambda_hyperparam = lambda_hyperparam
        self.n_iter = n_iter
        self.w = None
        self.b = None

    def initialise_params(self, X):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0

    def get_cls_map(self, y):
        # if y=0 then map to -1 else map to 1
        return np.where(y <= 0, -1, 1) # turns every class label of 0 into -1

    def get_gradient(self, x, idx):
        y = self.class_map[idx]
        # if data point lies on the correct side/ satisfies the constraint
        if y * (np.dot(x, self.w) + self.b) >= 1:
            dw = self.lambda_hyperparam * self.w
            db = 0
        else:
            dw = self.lambda_hyperparam * self.w - np.dot(y, x)
            db = - y
        return dw, db

    def update_params(self, dw, db):
        self.w -= self.lr_hyperparam * dw
        self.b -= self.lr_hyperparam * db

    def fit(self, X, y):
        '''
            Init weights and biases and map class labels form {0, 1} to {-1, 1}
        '''
        # init weights & biases
        self.initialise_params(X)
        # map binary class to {-1, 1}
        self.class_map = self.get_cls_map(y)
        '''
            Gradient Descent
        '''
        for _ in range(self.n_iter):
            for idx, x in enumerate(X):
                # compute the gradients
                dw, db = self.get_gradient(x, idx)
                # update the weights & biases
                self.update_params(dw, db)

    def predict(self, X):
        estimate = np.dot(X, self.w) + self.b
        prediction = np.sign(estimate)
        # map class from {-1, 1} to original values {0, 1}
        return np.where(prediction == -1, 0, 1)

def _accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)

def main():
    '''
        Create data
    '''
    X, y = datasets.make_blobs(
        n_samples=20, n_features=2, centers=2, cluster_std=1.05, random_state=1
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True, random_state=1)

    '''
        Test SVM
    '''
    clf = SVM(n_iter=10)
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)
    accuracy = _accuracy(y_test, predictions)
    print(f"Accuracy of SVM: {accuracy}")




if __name__ == '__main__':
    main()