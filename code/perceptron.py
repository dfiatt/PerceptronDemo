# perceptron.py
import numpy as np
import joblib

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=10):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size)
        self.bias = 0.0

    def activation(self, x):
        return np.where(x >= 0, 1, 0)

    def predict(self, x):
        return self.activation(np.dot(x, self.weights) + self.bias)

    def fit(self, X, y):
        n_samples = X.shape[0]
        error_history = []

        for epoch in range(self.epochs):
            errors = 0
            for i in range(n_samples):
                y_pred = self.predict(X[i])
                e = y[i] - y_pred  # Cálculo de error
                if e != 0:
                    # Actualización de pesos y sesgo
                    old_weights = self.weights.copy()
                    old_bias = self.bias
                    self.weights += self.lr * e * X[i]
                    self.bias += self.lr * e
                    errors += 1
            error_history.append(errors)
            print(f"Epoch {epoch+1}/{self.epochs} - Errores: {errors}")

        print("\nEntrenamiento finalizado.")
        print(f"Pesos finales: {self.weights}")
        print(f"Sesgo final: {self.bias}")
        print(f"Historial de errores por época: {error_history}")

    def save(self, filename="perceptron_model.pkl"):
        joblib.dump({'weights': self.weights, 'bias': self.bias}, filename)
        print(f"Modelo guardado en {filename}")

    def load(self, filename="perceptron_model.pkl"):
        data = joblib.load(filename)
        self.weights = data['weights']
        self.bias = data['bias']
        print(f"Modelo cargado desde {filename}")
