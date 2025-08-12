import numpy as np
import pickle

class Perceptron:
    def __init__(self, input_size, learning_rate=0.001, epochs=20):
        self.w = np.zeros(input_size)
        self.b = 0
        self.lr = learning_rate
        self.epochs = epochs
        
    def activation(self, z):
        return 1 if z > 0 else 0

    def predict(self, x):
        z = np.dot(self.w, x) + self.b
        return self.activation(z)

    def fit(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                z = np.dot(self.w, xi) + self.b
                y_hat = self.activation(z)
                update = self.lr * (target - y_hat)
                self.w += update * xi
                self.b += update

    def save(self, path="perceptron_model.pkl"):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    
     def load(path="perceptron_model.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)
