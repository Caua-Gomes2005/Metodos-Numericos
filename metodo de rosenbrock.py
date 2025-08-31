from sympy import symbols, diff
from numpy import transpose as tp, sqrt

x1, x2, lmb = symbols("x1 x2 lmb")

f = (x1-2)**4 + (x1-2*x2)**2

def mininewton(f, x0, direcao, e):
    
    c = f.subs({x1:(x0[0] + direcao[0]*lmb), x2:(x0[1]+ direcao[1]*lmb)})
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

def rosenbrock(x0, e):
    y0 = x0[:]
    j = 0
    d1 = [1,0]
    d2 = [0,1]

    #como vamos trabalhar com mais de um lambda é importante deixar eles já separados
    lamb1 = 0
    lamb2 = 0
    
    #coeficientes de gran schmidt
    a1 = [0,0]
    a2 = [0,0]

    while j<100:
        lamb1 = mininewton(f, y0, d1, e)
        y1 = [y0[0] + d1[0]*lamb1, y0[1] + d1[1]*lamb1]
        lamb2 = mininewton(f, y1, d2, e)
        y2 = [y1[0] + d2[0]*lamb2, y1[1] + d2[1]*lamb2]
        xl = y2[:]
        #calculo dos coeficientes de gran schmidt
        if lamb1 == 0:
                a1 = d1[:]
        else:
            d1 = [d1[0]*lamb1, d1[1]*lamb1]
            d2 = [d2[0]*lamb2, d2[1]*lamb2]
            a1 = [d1[0] + d2[0], d1[1] + d2[1]]
        b1 = a1[:]
        
        dl1 = [b1[0]/((b1[0]**2 + b1[1]**2)**0.5), b1[1]/((b1[0]**2 + b1[1]**2)**0.5)] #nova direção, d barra 1
        
        #para o segundo indice de coeficientes

        if lamb2 == 0:
                a2 = d2[:]
        else:
            d2 = [d2[0]*lamb2, d2[1]*lamb2]
            a2 = [d2[0], d2[1]]
        dlf = tp(dl1)
        b2 = a2 - (a2*dlf*dl1)
        dl2 = [b2[0]/((b2[0]**2 + b2[1]**2)**0.5), b2[1]/((b2[0]**2 + b2[1]**2)**0.5)]

        #direções sendo atualizadas
        d1 = dl1 
        d2 = dl2

        if abs(f.subs({x1:xl[0], x2:xl[1]}) - f.subs({x1:y1[0], x2:y1[1]})) < e: #criterio de parada, f(y2) - f(y1)<e
            break
        j =j+1
        y0 = xl
    print('Numero de iterações necessárias no total = ', j)
    
    return xl

x0 = [0,3]
xa = rosenbrock(x0, 0.0005) #vetor no ponto mínimo da função
d = f.subs({x1:xa[0], x2:xa[1]})
print('O vetor do ponto mínimo da função é = ', xa)
print('A função com o vetor aplicado nela = ', d)