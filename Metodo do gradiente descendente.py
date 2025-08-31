#Metodo do gradiente descendente

from sympy import symbols, diff

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

def graddes(x0, e):
    xl = x0
    df1 = diff(f, x1)
    df2 = diff(f, x2)
    grad = [df1.subs({x1:xl[0], x2:xl[1]}), df2.subs({x1:xl[0], x2:xl[1]})]
    modulo = (grad[0]**2 + grad[1]**2)**0.5
    d = [-grad[0]/modulo, -grad[1]/modulo]
    lamb = mininewton(f, xl, d, e)
    k = 0
    xh = [xl[0] + lamb*d[0], xl[1] + lamb*d[1]]
    while k < 100:
        xl = xh
        grad = [df1.subs({x1:xl[0], x2:xl[1]}), df2.subs({x1:xl[0], x2:xl[1]})]
        modulo = (grad[0]**2 + grad[1]**2)**0.5
        d = [-grad[0]/modulo, -grad[1]/modulo]
        lamb = mininewton(f, xl, d, e)
        xh = [xl[0] + lamb*d[0], xl[1] + lamb*d[1]]
        if abs(f.subs({x1:xh[0], x2:xh[1]}) - f.subs({x1:xl[0], x2:xl[1]})) < e: #criterio de parada, f(x1) - f(x0)<e
            break
        k = k+1
    print(k)
    return xh

x0 = [0,3]

c = graddes(x0, 5e-5)

d = f.subs({x1:c[0], x2:c[1]})
print('O vetor do ponto mínimo da função é = ', c)
print('A função com o vetor aplicado nela = ', d)






