# import required modules
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

#paths
APP_FOLDER = os.path.dirname(__file__)
FILES_FOLDER = os.path.dirname(APP_FOLDER)
FILES_FOLDER = os.path.join(FILES_FOLDER, "files")

def init_globals(time, hw, hb, ow, ob):
    global inputs, file_columns, courses_grades
    global hidden_weights, hidden_bias
    global output_weights, output_bias

    #inputs
    filename = "\{time}standarfile.csv".format(time=time)
    data = pd.read_csv(FILES_FOLDER+filename)
    scaler = MinMaxScaler()

    # get courses grades
    courses_grades = data.iloc[:, :].values

    # get scaled inputs and excepted outputs
    x = scaler.fit_transform(data.iloc[:, :].values)

    # define inputs and expected outputs
    inputs = np.array(x)

    # define which columns would contain the file
    file_columns = ["MATEMATICA", "COMUNICACION", "PFRH", "CIENCIAS SOCIALES", "CIENCIA TECNOLOGIA Y AMBIENTE", "UNIV A", "UNIV B"]

    # get weights and bias
    """hidden_weights = [[18.559973393217064, 20.814059984135657, 17.61786519642371], 
                    [18.220043981622013, 21.70416985697831, 17.762354424426036], 
                    [18.52629260163194, 21.609404376910376, 19.09913891993568], 
                    [20.605168994266748, 22.0015356443664, 17.714787497944762], 
                    [20.734617945304183, 22.283033863866123, 17.747173494154346]] 
    hidden_bias = [[-32.998345353689224, -32.71893708119303, -30.978028990682105]] 
    output_weights = [[-0.05144790134264302, 0.30548578656117353], 
                    [0.3652853211862023, 0.003255147367954442], 
                    [-0.23342630287255503, -0.013830922146140642]] 
    output_bias = [[-5.457835365043566, -5.125684230385598]]"""
    hidden_weights = hw
    hidden_bias = hb
    output_weights = ow
    output_bias = ob

# function to get the sigmoid value of an array
def sigmoid(x):
    return 1/(1+np.exp(-x))

# function to frontpropagate and predict the inputs
def frontpropagation(inputs, hidden_weights, hidden_bias, output_weights, output_bias):
    # frontpropagate of the inputs to the first hidden layer
    hidden_layer_activation = np.dot(inputs, hidden_weights) + hidden_bias
    
    # frontpropagate of the hidden layer to the ouput layer
    output_layer_activation = np.dot(hidden_layer_activation, output_weights) + output_bias
    output_layer_output = sigmoid(output_layer_activation)

    return output_layer_output

# create file to export
def create_file(file_matrix, time):    
    file = pd.DataFrame(file_matrix, columns = file_columns)
    filename = "\{time}predicted_file.csv".format(time=time)
    file.to_csv(FILES_FOLDER+filename, index = False, header = True)

# predict if the student entered to the universities
def Predict_Inputs(time, hw, hb, ow, ob):
    init_globals(time, hw, hb, ow, ob)
    predicted_values = frontpropagation(inputs, hidden_weights, hidden_bias, output_weights, output_bias)
    file_matrix = np.append(courses_grades, np.round(predicted_values), 1)
    create_file(file_matrix, time)

#predict_inputs()