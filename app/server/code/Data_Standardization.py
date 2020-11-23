# import required modules
import pandas as pd
import numpy as np
import os

#paths
APP_FOLDER = os.path.dirname(__file__)
FILES_FOLDER = os.path.dirname(APP_FOLDER)
FILES_FOLDER = os.path.join(FILES_FOLDER, "files")

# assignment of the five 'areas' and the possible courses
courses = ["MATEMATICA", "COMUNICACION", "PFRH", "CIENCIAS SOCIALES", "CIENCIA TECNOLOGIA Y AMBIENTE"]

# initialization of the arrays of each 'area'   
matematica   = []
comunicacion = []
pfrh         = []
ccss         = []
cta          = []
predicted    = []
matrixScore  = []

# add the data in the 'area'
def AppendInArea(course, area):
    temp = list(data[course].iloc[:])
    area.append(temp)
 
# calculate the average of an 'area'
def AverageArea(area):
    arrayAverage = []
    summation = 0
    for c in range(len(area[0])):
        for f in range(len(area)):
            summation += area[f][c]
        average = summation/len(area)
        arrayAverage.append(average)
        summation = 0
    return arrayAverage 

# create file to export
def CreateFile(matrix, courses, time):    
    file = pd.DataFrame(matrix, columns = courses)
    flname = "\{time}standarfile.csv".format(time=time)
    file.to_csv(FILES_FOLDER+flname, index = False, header = True)

# standardize student data
def Standardization(filename, time):
    # get the data and courses
    global data
    data = pd.read_csv(filename)
    datacourses = [ c for c in data]

    for course in datacourses:
        if(course == "MATEMATICA" or course == "RAZ MATEMATICO" or course == "ARITMETICA" or course == "GEOMETRIA" or course == "ALGEBRA" or course == "TRIGONOMETRIA"):
            AppendInArea(course, matematica)
            continue
        if (course == "LENGUAJE" or course == "LITERATURA" or course == "RAZ VERBAL" or course == "COMUNICACION"):
            AppendInArea(course, comunicacion)
            continue        
        if (course == "PSICOLOGIA" or course == "EDUCACION CIVICA" or course == "PFRH"):
            AppendInArea(course, pfrh)
            continue
        if (course == "HPERU" or course == "HUNIV" or course == "GEOGRAFIA" or course == "ECONOMIA" or course == "FILOSOFIA" or course == "CIENCIAS SOCIALES"):
            AppendInArea(course, ccss)
            continue
        if (course == "FISICA" or course == "QUIMICA" or course == "BIOLOGIA" or course == "CIENCIA TECNOLOGIA Y AMBIENTE"):
            AppendInArea(course, cta)
            continue

    # average all 'areas'
    matrixScore.append(AverageArea(matematica))
    matrixScore.append(AverageArea(comunicacion))
    matrixScore.append(AverageArea(pfrh))
    matrixScore.append(AverageArea(ccss))
    matrixScore.append(AverageArea(cta))

    # add predictions if 'areas' columns are present
    if datacourses[-1] == "UNIV B":
        AppendInArea("UNIV A", predicted)
        AppendInArea("UNIV B", predicted)
        matrixScore.append(predicted[0])
        matrixScore.append(predicted[1])
        courses.append("UNIV A")
        courses.append("UNIV B")
    
    matrix = np.array(matrixScore).T
    CreateFile(matrix, courses, time)
