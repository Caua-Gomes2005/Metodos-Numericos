from sympy import symbols, diff, cos

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

def methj(x0, e):
    y0 = x0[:]
    k = 0
    while k<100:
        d1 = [1,0]
        d2 = [0,1]
        lamb = mininewton(f, y0, d1, e)
        y1 = [y0[0] + d1[0]*lamb, y0[1] + d1[1]*lamb]
        lamb = mininewton(f, y1, d2, e)
        y2 = [y1[0] + d2[0]*lamb, y1[1] + d2[1]*lamb]
        d = [y2[0] - y0[0],y2[1] - y0[1]]
        lamb = mininewton(f, y2, d, e)
        xl = [y2[0] + d[0]*lamb, y2[1] + d[1]*lamb]
        if abs(f.subs({x1:xl[0], x2:xl[1]}) - f.subs({x1:y1[0], x2:y1[1]})) < e: #criterio de parada, f(x1) - f(x0)<e
            break
        y0 = xl[:]
        k = k+1
    print('Numero de iterações necessárias no total = ', k) 
    return xl

x0 = [0, 3] #ponto inicial
xa = methj(x0,0.000005) #vetor no ponto mínimo da função

d = f.subs({x1:xa[0], x2:xa[1]})
print('O vetor do ponto mínimo da função é = ', xa)
print('A função com o vetor aplicado nela = ', d)
