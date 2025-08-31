import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt

def f(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1] + 4*x[0] + 4*x[1]

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

