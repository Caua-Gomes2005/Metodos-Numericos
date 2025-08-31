import numpy as np

from sympy import symbols, diff

x1, x2 = symbols('x1 x2')
f = x1**x1 - 49
x0 =[0,3]

e = 0.05
def newmv(f, x0, e):
    k = 0
    xl = np.array(x0)
    dfx1 = diff(f, x1)
    dfx2 = diff(f, x2)
    df2x1 = diff(f, x1, 2)
    df2x2 = diff(f, x2, 2)
    dfx1x2 = diff(dfx1, x2)
    g = np.array([dfx1.subs({x1:xl[0], x2:xl[1]}), dfx2.subs({x1:xl[0], x2:xl[1]})])
    hes = np.array([[float(df2x1.subs({x1:xl[0], x2:xl[1]})),float(dfx1x2.subs({x1:xl[0], x2:xl[1]}))], 
                    [float(dfx1x2.subs({x1:xl[0], x2:xl[1]})), float(df2x2.subs({x1:xl[0], x2:xl[1]}))]])
    ih = np.linalg.inv(hes)
    
    xh = xl - np.dot(g, ih)
    
    while abs((xh[0]** + xh[1]**2)**0.5 - (xl[0]** + xl[1]**2)**0.5) > e: 
        xl = xh
        grad = [dfx1.subs({x1:xl[0], x2:xl[1]}), dfx2.subs({x1:xl[0], x2:xl[1]})]
        g = np.array(grad)
        hes = [[float(df2x1.subs({x1:xl[0], x2:xl[1]})),float(dfx1x2.subs({x1:xl[0], x2:xl[1]}))], 
               [float(dfx1x2.subs({x1:xl[0], x2:xl[1]})), float(df2x2.subs({x1:xl[0], x2:xl[1]}))]]
        ih = np.linalg.inv(hes)
        xh = xl - np.dot(g, ih)
        k = k+1
        if k > 100:
            break
        print(xh)
    print('k = ', k)
    
    return xh

r = newmv(f, x0, 5e-5)
print(r)
print(f.subs({x1:r[0], x2:r[1]}))   
    

