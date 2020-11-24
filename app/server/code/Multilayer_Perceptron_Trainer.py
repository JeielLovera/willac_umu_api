# import required modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

#paths
APP_FOLDER = os.path.dirname(__file__)
FILES_FOLDER = os.path.dirname(APP_FOLDER)
FILES_FOLDER = os.path.join(FILES_FOLDER, "files")

# function to frontpropagate the inputs
def frontpropagation(inputs, hidden_weights, hidden_bias, output_weights, output_bias):
    # frontpropagate of the inputs to the first hidden layer
    hidden_layer_activation = np.dot(inputs, hidden_weights) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)
    
    # frontpropagate of the hidden layer to the ouput layer
    output_layer_activation = np.dot(hidden_layer_activation, output_weights) + output_bias
    output_layer_output = sigmoid(output_layer_activation)

    return output_layer_output, hidden_layer_output

# function to backpropagate the error and train the neural network
def backpropagation(inputs, expected_output, output_layer_output, output_weights, output_bias, hidden_layer_output, hidden_weights, hidden_bias, paths):
    # do not propagate -1 values (did not took the exam)
    for i in range(len(expected_output)):
        for j in range(len(expected_output[i])):
            if(expected_output[i][j] == -1):
                output_layer_output[i][j] == -1
    # calculate the ouput layer's predicted delta
    output_predicted_error = expected_output - output_layer_output
    output_predicted_d = sidgmoid_derivative(output_layer_output)*output_predicted_error

    # calculate the hidden layer's predicted delta
    hidden_predicted_error = output_predicted_d.dot(output_weights.T)
    hidden_predicted_d = sidgmoid_derivative(hidden_layer_output)*hidden_predicted_error

    # update wights and bias
    output_weights += hidden_layer_output.T.dot(output_predicted_d)*lr/paths
    output_bias += np.sum(output_predicted_d)*lr/paths
    hidden_weights += inputs.T.dot(hidden_predicted_d)*lr/paths
    hidden_bias += np.sum(hidden_predicted_d)*lr/paths

# function to calculate the instant error
def calculateError(expected_output, output_layer_output, error_history):
    # do not consider -1 values (did not took the exam)
    valid_values = len(expected_output[0])
    for i in range(len(expected_output[0])):
        if(expected_output[0][i] == -1):
            output_layer_output[0][i] == -1
            valid_values -= 1
    # calculate the instant error 
    expected_dif = (expected_output - output_layer_output)
    dif_cuadrada = np.power(expected_dif, 2)
    inst_error = np.sum(dif_cuadrada.T)/valid_values
    error_history.append(inst_error)

# function to get the sigmoid value of an array
def sigmoid(x):
    return 1/(1+np.exp(-x))

# function to get the sigmoid derivative of an array
def sidgmoid_derivative(x):
    return x*(1+x)

def learning_stage(learning_data, learning_expected_output, hidden_weights, hidden_bias, output_weights, output_bias):
    # define number of elements in the learning data array
    learning_elements = len(learning_data)

    # frontpropagation
    output_layer_output, hidden_layer_output = frontpropagation(learning_data, hidden_weights, hidden_bias, output_weights, output_bias)

    # backpropagation
    backpropagation(learning_data, learning_expected_output, output_layer_output, output_weights, output_bias, hidden_layer_output, hidden_weights, hidden_bias, learning_elements)

def testing_stage(testing_data, testing_expected_output, error_history):
    # frontpropagation
    output_layer_output, _ = frontpropagation(testing_data, hidden_weights, hidden_bias, output_weights, output_bias)

    # calculate epoch error
    calculateError(testing_expected_output, output_layer_output, error_history)

def init_globals(time):
    global data, scaler, x, y, inputs, expected_output, epochs, lr, model_error
    global input_layer_neurons, hidden_layer_neurons, output_layer_neurons, steps, paths
    global error_history, hidden_weights, output_weights, hidden_bias, output_bias

    #inputs
    filename = "\{time}standarfile.csv".format(time=time)
    data = pd.read_csv(FILES_FOLDER+filename)
    scaler = MinMaxScaler()

    # get scaled inputs and excepted outputs
    x = scaler.fit_transform(data.iloc[:, :-2].values)
    y = data.iloc[:, -2:].values

    # define inputs and expected outputs
    inputs = np.array(x)
    expected_output = np.array(y)

    # neural network training attributes
    paths = len(inputs)
    n_multiplicity = 5
    epochs = paths*n_multiplicity
    lr = 0.25
    input_layer_neurons, hidden_layer_neurons, output_layer_neurons = 5, 3, 2
    steps = range(epochs)
    
    # error history
    error_history = []
    model_error = 0

    # random weights
    output_weights = np.random.uniform(0, 1, size=(hidden_layer_neurons, output_layer_neurons))
    hidden_weights = np.random.uniform(18, 21, size=(input_layer_neurons, hidden_layer_neurons))
    # random bias
    hidden_bias = np.random.uniform(-31, -28, size=(1, hidden_layer_neurons))
    output_bias = np.random.uniform(-5, -4, size=(1, output_layer_neurons))

def Multilayer_Perceptron_Trainer(time):
    init_globals(time)
    for i in range(epochs):
        # divide learning data and testing data
        testing_data = np.array([inputs[i%paths]])
        learning_data = np.delete(inputs, i%paths, 0)
        testing_expected_output = np.array([expected_output[i%paths]])
        learning_expected_output = np.delete(expected_output, i%paths, 0)
        
        # learning stage
        learning_stage(learning_data, learning_expected_output, hidden_weights, hidden_bias, output_weights, output_bias)
        
        # testing stage
        testing_stage(testing_data, testing_expected_output, error_history)

        # in the last epoch calculate the model error
        if(i == epochs-1):
            model_error = np.sum(error_history)/(epochs)
    
    # plot error
    plt.plot(steps, error_history, label='Error History')

    plt.xlabel('Time (steps)')
    plt.ylabel('Error')
    plt.title('Evolution of Error vs Time')

    plt.legend()
    imgname = "/{time}error.png".format(time=time)
    plt.savefig(FILES_FOLDER+imgname)

    hw = [[x for x in y] for y in hidden_weights]
    hb = [[x for x in y] for y in hidden_bias]
    ow = [[x for x in y] for y in output_weights]
    ob = [[x for x in y] for y in output_bias]

    plt.clf()
    plt.cla()

    return (hw, hb, ow, ob)

