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

for epoch in range(epochs):
    # Forward Propogation
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_input)

    # Back Propogation
    error = y - final_output

    output_gradient = error * sigmoid_derivative(final_output)
    
    hidden_error = output_gradient.dot(weights_hidden_output.T)
    hidden_gradient = hidden_error * sigmoid_derivative(hidden_output)

    weights_input_hidden += X.T.dot(hidden_gradient) * learning_rate
    bias_hidden += np.sum(hidden_gradient, axis=0, keepdims=True) * learning_rate

    if epoch % 1000 == 0:
        loss = np.mean(np.abs(error))
        print(f"Epoch {epoch}, Loss: {loss:.5f}")


