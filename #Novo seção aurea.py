#Novo seção aurea

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
from sympy import symbols, diff



rands = np.random.uniform(0,1000,5)
database = []
for i in range(0,len(rands)):
    database.append({'Amplitude': rands[i], 'pulso(1)': 0*rands[1], 'pulso(2)': 0.0172*rands[1], 'pulso(3)': 0.4524*rands[1], 
                     'pulso(4)': 1*rands[1], 'pulso(5)': 0.5633*rands[1], 'pulso(6)': 0.1493*rands[1], 'pulso(7)': 0.0424*rands[1]})
data_base = pnd.DataFrame(database)
data_base.to_csv('L:/Facul/Quarto Periodo/Codigos/basededados.csv')

line = 1
Pulso = pnd.read_csv('L:/Facul/Quarto Periodo/Codigos/basededados.csv', skiprows = line, nrows=1).values 
Pulso = list(Pulso[0]) #Xi
del Pulso[0:2]
print(Pulso)

Pog = list(0, 0.0172, 0.4524, 0.5633, 0.1493, 0.0424)

A = symbols('A')
Amplitudes = [] #Amplitude

função = (Pulso[i] - A*Pog[i])**2