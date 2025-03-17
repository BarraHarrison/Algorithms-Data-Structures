# BackPropogation Algorithm vital part of training deep neural networks
# Reduxes error on predictions using gradient descent 
# The neural network makes better predictions as a result

# How a small neural network with one hidden layer uses backpropogation

import numpy as np 

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training Data
# X is inputs and y is the target outputs
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]   
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])