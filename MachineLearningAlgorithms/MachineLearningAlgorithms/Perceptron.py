import numpy as np
class Perceptron(object):
    """Perceptron Classifier
    
    Parameters: 
        eta: float
            Learning Rate (between 0.0 and 1.0)
        
        n_iter: int
            Number of passes over the training dataset

    Attributes:
        w_ : 1d-array
            weights after fitting

        errors_ : list
            Number of misclassifcations in every epoch
    
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, Y):
        """Fit training data

        Parameters
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features.

        Y: array-like, shape = [n_samples]
            Target values

        Returns
            self : object
        """
        self.w_ = np.zeros(1 + X.shape[1])


