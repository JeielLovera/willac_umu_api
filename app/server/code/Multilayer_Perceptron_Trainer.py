# import required modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os


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
def backpropagation(expected_output, output_layer_output, output_weights, output_bias, hidden_layer_output, hidden_weights, hidden_bias, paths):
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
def calculateError(expected_output, output_layer_output, error_history, paths):
    # calculate the instant error 
    expected_dif = (expected_output - output_layer_output)
    dif_cuadrada = np.power(expected_dif, 2)
    inst_error = np.sum(dif_cuadrada.T, 1)/paths
    for i in range(len(error_history)):
        error_history[i].append(inst_error[i])
    return inst_error

# function to print the results of an epoch
def printResults(i, hidden_weights, output_weights, hidden_bias, output_bias, inst_error):
    # print the results
    print()
    print("Epoch", i)
    print('Pesos de la capa oculta', hidden_weights)
    print('Pesos de la capa salida', output_weights)
    print('Bias de la capa oculta', hidden_bias)
    print('Bias de la capa salida', output_bias)
    print('El error instantaneo', inst_error)
    print()

# function to get the sigmoid value of an array
def sigmoid(x):
    return 1/(1+np.exp(-x))

# function to get the sigmoid derivative of an array
def sidgmoid_derivative(x):
    return x*(1+x)

# inputs
# get scaled inputs and excepted outputs
# error history
# random weights
# random bias

"""print('Inputs', inputs)
print('Outputs', expected_output)
print('Pesos de la capa oculta', hidden_weights)
print('Pesos de la capa salida', output_weights)
print('Bias de la capa oculta', hidden_bias)
print('Bias de la capa salida', output_bias)
"""
def TrainingNeuralNetwork(time):
    global data, scaler, x, y, inputs, expected_output, epochs, lr
    global input_layer_neurons, hidden_layer_neurons, output_layer_neurons, steps, paths
    global error_history, hidden_weights, output_weights, hidden_bias, output_bias

    #inputs
    filename = "\{time}standarfile.csv".format(time=time)
    data = pd.read_csv(FILES_FOLDER+filename)
    scaler = MinMaxScaler()

    # get scaled inputs and excepted outputs
    x = scaler.fit_transform(data.iloc[:, :-2].values)
    y = data.iloc[:, -2:].values

    inputs = np.array(x)
    expected_output = np.array(y)

    epochs = 10000
    lr = 0.25
    input_layer_neurons, hidden_layer_neurons, output_layer_neurons = 5, 3, 2
    steps = range(epochs)
    paths = len(inputs)
    
    # error history
    error_history = [[], []]

    # random weights
    hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
    output_weights = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))

    # random bias
    hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
    output_bias = np.random.uniform(size=(1, output_layer_neurons))

    #training
    for i in range(epochs):
        
        # aprendizaje:
        # frontpropagation
        output_layer_output, hidden_layer_output = frontpropagation(inputs, hidden_weights, hidden_bias, output_weights, output_bias)

        # backpropagation
        backpropagation(expected_output, output_layer_output, output_weights, output_bias, hidden_layer_output, hidden_weights, hidden_bias, paths)
        

        # calculate epoch error
        inst_error = calculateError(expected_output, output_layer_output, error_history, paths)
        
        # print results every 100 epochs
        """if(i % 100 == 0):
            printResults(i, hidden_weights, output_weights, hidden_bias, output_bias, inst_error)"""

        # stop condition
        if(inst_error[0] < 0.01 and inst_error[1] < 0.01 or i == epochs - 1):
            #printResults(i, hidden_weights, output_weights, hidden_bias, output_bias, inst_error)
            steps = range(i+1)
            #print("Última época", i)
            break

    # plot error
    plt.plot(steps, error_history[0], label='Error Univ A')
    plt.plot(steps, error_history[1], label='Error Univ B')

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
    return (hw, hb, ow, ob)
    #plt.show()

# neural network testing
"""TrainingNeuralNetwork('/standarfile.csv')
for i in range(4):
    x1, x2, x3, x4, x5 = input().split(" ")
    inputs_to_predict = np.array([[float(x1), float(x2), float(x3), float(x4), float(x5)]])
    result, _ = frontpropagation(inputs_to_predict, hidden_weights, hidden_bias, output_weights, output_bias)
    print(result)"""

"""if __name__ == "__main__":
    TrainingNeuralNetwork('/standarfile.csv')
    arr = [[x for x in y] for y in hidden_weights]
    print(arr)
    print(hidden_bias)
    print()
    print(output_weights)
    print()
    print(output_bias)"""