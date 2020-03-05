import numpy as np
from typing import Tuple

def loss_function(dots:Tuple[int, int], weight: np.array):
    # Squared error
    return sum((weight.dot(x) - y) ** 2 for x,y in dots) / len(dots)

def loss_derivative(dots:Tuple[int, int], weight: np.array):
    # Derivative in respect to w of squared error
    return sum((2 * (weight.dot(x) - y) * x) for x,y in dots) / len(dots)

lr = 0.01

#Generate data
true_weight = np.array([1, 2, 3, 4, 5])
dim = len(true_weight)
dots = []
for i in range(100):
    x = np.random.randn(dim).dot(true_weight)
    y = true_weight.dot(x) + np.random.randn()
    dots.append((x, y))

def gradient_descent(loss_function, loss_derivative, dim):
    weight = np.zeros(dim)
    for i in range(10):
        loss = loss_function(dots, weight)
        gradient = loss_derivative(dots, weight)

        print(f'Loss: {loss}, gradient: {gradient}, weight: {weight}')
        weight = weight - lr * gradient

gradient_descent(loss_function, loss_derivative, dim)