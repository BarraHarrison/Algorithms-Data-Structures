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

# Initialize neural network parameters
np.random.seed(42)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Initialize the weights and biases
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

# Training Parameters
learning_rate = 0.5
epochs = 10000