#metodo fletcher reeves

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

def fr(f,x0, e):
    k=1
    j=1
    y1 = np.array(x0)
    y2 = 10*y1
    df1 = diff(f, x1)
    df2 = diff(f, x2)
   
    while j < 3:
        if j == 1:
            g1 = np.array([df1.subs({x1:y1[0], x2:y1[1]}), df2.subs({x1:y1[0], x2:y1[1]})])
            d = -g1
            d1 = d
            j = j+1
        else:
            g2 = np.array([df1.subs({x1:y2[0], x2:y2[1]}), df2.subs({x1:y1[0], x2:y1[1]})])
            alp = (g2[0]**2 + g2[1]**2)/(g1[0]**2 + g1[1]**2)
            d = -g2 + alp*d1
            j = 1
        lamb = mininewton(f, y2, d, e)
        y2 = y1 + lamb*d
        if abs((y2[0]** + y2[1]**2)**0.5 - (y1[0]** + y1[1]**2)**0.5) < e:
            break
        y1 = y2
        k = k+1
        print(y1)
    return y1

x0 = [0,3]
r = fr(f, x0, 5e-5)
print(r)
print(f.subs({x1:r[0], x2:r[1]}))   
