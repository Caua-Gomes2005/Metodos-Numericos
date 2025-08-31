import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from sympy import symbols, diff

A =symbols('A')
rp = []
for i in range(10000):
    rp.append(rnd.uniform(0,10000))
print(rp)

x0 =[0, 0.0172, 0.4524, 1, 0.5633, 0.1443, 0.0424] #estimativa inicial

f = (x0[i]-A*rp[i])**2
df = diff(f, A)
df2= diff(f, A, 2)

def funcao(x): #função
    return (x-2)**4 + (x-6)*2


e = 0.000005 #tolerancia
print('x0: ', x0)
def mininewton(x0, e):
    x1 = x0 - (df.subs({x:x0}))/(df2.subs({x:x0})) #calculo do x1 antes de entrar no laço
    k=0
    while abs(x1-x0) > e:
        x0 = x1
        x1 = x0 - (df.subs({x:x0}))/(df2.subs({x:x0}))
        k = k+1
        print('x0: ', x0, 'x1: ', x1, 'iteração: ', k)
        if k>200: #cão de guarda para impedir muitas iterações
            break
    return float(x1+x0)/2

c = mininewton(x0, e)

print("O valor aproximado que minimiza a função é: ", c)
print("E aplicado na função resulta em: ", funcao(c))

xp = np.linspace(-25, 25, 100)
plt.plot(c,funcao(c), 'bo') #ponto otimizado
plt.plot(xp, funcao(xp), color='red') #função para visualização
plt.show()