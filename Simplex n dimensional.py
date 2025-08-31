import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt


def simplex(x0, tol, maxit):
    n = len(x0)
    splx = x0[:]
    k = 0

    for iterações in range(maxit):
        #ORDENAÇÂO DO SIMPLEX

        splx.sort(key=lambda x: f(x))

        #Calculo do centroide

        centroide = np.mean(splx[:-1], axis=0)

        #REFLEXÃO

        xr = centroide + (centroide - splx[-1])

        if f(xr) < f(splx[0]):
            
            #EXPANSÃO
            xe = centroide + 2*(xr - centroide)
            if f(xe) < f(xr):
                splx[-1]=xe
            else:
                splx[-1]=xr
        elif f(xr)< f(splx[-2]):
            splx[-1] = xr
        else:
            #CONTRAÇÃO
            xc = centroide + 0.5*(splx[-1] - centroide)
            if f(xc)< f(splx[-1]) :
                splx[-1] = xc
                
                    
            else: #REDUÇÃO
                for i in range(1, len(splx)):
                    splx[i] = splx[0] + 0.5*(splx[i] - splx[0])
    
        #convergencia
        if np.std([f(x) for x in splx]) < tol:
            break
        splx.sort(key=lambda x: f(x))
        k= k+1
    print(k)
    return splx[0]

n = 50

rands = np.random.uniform(0,1000,n)
database = []
for i in range(0,len(rands)):
    database.append({'Amplitude': rands[i], 'pulso(1)': 0*rands[i], 'pulso(2)': 0.0172*rands[i], 'pulso(3)': 0.4524*rands[i], 
                     'pulso(4)': 1*rands[i], 'pulso(5)': 0.5633*rands[i], 'pulso(6)': 0.1493*rands[i], 'pulso(7)': 0.0424*rands[i]})
data_base = pnd.DataFrame(database)
data_base.to_csv('L:/Facul/Quarto Periodo/Codigos/basededados.csv')




v = [[1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0]]

erros = []
t=n

for line in range(0,n):
    Pulso = pnd.read_csv('L:/Facul/Quarto Periodo/Codigos/basededados.csv', skiprows = line, nrows=1).values 
    Pulso = list(Pulso[0]) #Xi
    del Pulso[0:2]

    def f(A):
        signals = [A[0]*1 + A[1]*0.4524 + A[2]*0.0172 + 0 + 0 + 0 + 0,
                A[0]*0.5633 + A[1]*1 + A[2]*0.4524 + A[3]*0.0172 + 0 + 0 + 0,
                A[0]*0.1493 + A[1]*0.5633 + A[2]*1 + A[3]*0.4524 + A[4]*0.0172 + 0 + 0,
                A[0]*0.0424 + A[1]*0.1493 + A[2]*0.5633 + A[3]*1 + A[4]*0.4524 + A[5]*0.0172 + 0,
                0 + A[1]*0.0424 + A[2]*0.1493 + A[3]*0.5633 + A[4]*1 + A[5]*0.4524 + A[6]*0.0172,
                0 + 0 + A[2]*0.0424 + A[3]*0.1493 + A[4]*0.5633 + A[5]*1 + A[6]*0.4524,
                0 + 0 + 0 + A[3]*0.0424 + A[4]*0.1493 + A[5]*0.5633 + A[6]*1]
        Sum = 0
        for i in range(0, len(Pulso)):
            Sum += (Pulso[i]-signals[i])**2
        return 1/len(Pulso)*Sum**0.5
    r = simplex(v,1e-50,10000)
    erro = r[3] - Pulso[3]
    print(erro)
    erros.append(erro)
    t = t-1
    print(t)

plt.hist(erros)
plt.xlabel('erros')
plt.ylabel('quantidade')
plt.show()