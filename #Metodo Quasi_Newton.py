#Metodo Quasi_Newton

from sympy import symbols, diff
import numpy as np

x1, x2, lmb = symbols("x1 x2 lmb")

f = (x1-2)**4 + (x1-2*x2)**2

def mininewton(f, x0, direcao, e):
    
    c = f.subs({x1:x0[0] + direcao[0]*lmb, x2:x0[1]+ direcao[1]*lmb})
    dc1 = diff(c,lmb)
    dc2 = diff(c, lmb, 2)
    xl = 0
    xh = xl - (dc1.subs({lmb:xl}))/(dc2.subs({lmb:xl})) #calculo do x1 antes de entrar no laço
    k=0
    while abs(xh-xl) > e:
        xl = xh
        xh = xl - (dc1.subs({lmb:xl}))/(dc2.subs({lmb:xl}))
        k = k+1
        if k>200: #cão de guarda para impedir muitas iterações
            break
    return float((xh+xl)/2)

def quasinewton(f, x0, e):
    xl = np.array(x0)
    n = 2
    k = 1
    j = 1
    fx1 = diff(f, x1)
    fx2 = diff(f,x2)
    xh = 10*xl
    
    while abs((xh[0]**2 + xh[1]**2)**0.5 - (xl[0]**2 + xl[1]**2)**0.5) > e:
            xl = xh
            j = 1
            g1 = [fx1.subs({x1:xl[0], x2:xl[1]}), fx2.subs({x1:xl[0], x2:xl[1]})]
            
            D1 = [[1,0], 
                  [0,1]]
            d1 = np.array(-np.dot(D1,g1))
            lamb = mininewton(f,xl, d1, 0.005)
            xh = xl + lamb*d1
            p = np.array([[xh[0]-xl[0]],[xh[1]-xl[1]]])
            tp = np.transpose(p)
            q = np.array([[fx1.subs({x1:xh[0], x2:xh[1]}) - fx1.subs({x1:xl[0], x2:xl[1]})],[fx2.subs({x1:xh[0], x2:xh[1]}) - fx2.subs({x1:xl[0], x2:xl[1]})]])
            tq = np.transpose(q)
            if j < n:
                 D2 = D1 + p*tp/(np.matmul(tp, q)) - q*tq/(np.matmul(tq,q))
                 g2 = [fx1.subs({x1:xh[0], x2:xh[1]}), fx2.subs({x1:xh[0], x2:xh[1]})]
                 d2 = np.array(-np.dot(D2,g2))
                 lamb = mininewton(f, xh, d2, 0.005)
                 xl = xh
                 xh = xl + lamb*d2
                 j = j +1
            k= k+1
        
            if k>201:
                 break
            
           
    print(k)
    return xh

x0 = [0,3]
r = quasinewton(f, x0, 5e-5)
rf = f.subs({x1:r[0], x2:r[1]})

print(r)
print(rf)

