import numpy as np
import random
import time
from typing import Tuple, Callable, List
from dataclasses import dataclass

random.seed(0)

@dataclass
class Point:
    x:np.array
    y:int

    def __iter__(self):
        yield self

    def __len__(self):
        return 1


def loss_function(points: Point, weight: np.array):
    # Squared error
    return sum((weight.dot(point.x) - point.y) ** 2 for point in points) / len(points)


def loss_derivative(points: Point, weight: np.array):
    # Derivative in respect to w of squared error
    return sum((2 * (weight.dot(point.x) - point.y) * point.x) for point in points) / len(points)


# Generate data
true_weight = np.array([1, 2, 3, 4, 5])
dim = len(true_weight)
points = []
for i in range(10000):
    x = np.random.randn(dim)
    y = true_weight.dot(x) + np.random.randn()
    points.append(Point(x=x, y=y))


def gradient_descent(loss_function:Callable, loss_derivative:Callable, points:Point, lr=0.01):
    dim = len(points[0].x)
    weight = np.zeros(dim)
    for i in range(10):
        loss = loss_function(points, weight)
        gradient = loss_derivative(points, weight)
        weight = weight - lr * gradient

        print(f'Iteration: {i}, Loss: {loss}, weight: {weight}')


def stochastic_gradient_descent(loss_function:Callable, loss_derivative:Callable, points:Point):
    dim = len(points[0].x)
    weight = np.zeros(dim)
    for i in range(10):
        # Mini batching with random selection
        for point in random.choices(points, k=int(len(points)/10)):
            loss = loss_function(point, weight)
            gradient = loss_derivative(point, weight)
            lr = 1 / (len(points)/100)
            weight = weight - lr * gradient

        print(f'Iteration: {i+1}, Loss: {loss}, weight: {weight}')


print('Gradient Descent...')
start = time.time()
gradient_descent(loss_function, loss_derivative, points)
elapsed_time = time.time() - start
print(f'Elapsed time: {elapsed_time}')

print('\nStochastic Gradient Descent...')
start = time.time()
stochastic_gradient_descent(loss_function, loss_derivative, points)
elapsed_time = time.time() - start
print(f'Elapsed time: {elapsed_time}')
