import pandas as pd

scores = ["ARTE,CTA,COMUNICACION,EFIS,ETRA,EREL,FCC,PSICOLOGIA,LITERATURA,ECONOMIA,HPERU,FISICA,ALGEBRA,ARITMETICA,PFRRHH,UNIV A,UNIV B","17,19,18,18,17,18,18,18,20,19,18,17,19,18,19,1,1","17,16,15,15,17,16,16,16,18,17,18,15,17,16,15,1,1","17,16,16,16,17,17,15,16,18,17,14,13,15,14,16,0,1","16,16,16,16,16,15,15,17,19,18,16,15,17,16,16,1,1"]
columns = scores[0].split(',')
matrixscores = [ [float(l) for l in line.split(",")] for line in scores[1:]]
data = pd.DataFrame(matrixscores, columns = columns)

datacourses = [ c for c in data]



from datetime import datetime

now = datetime.now()
time = now.strftime("%H%M%S")

flname = "\{time}standarfile.csv".format(time=time)
print(flname)