#Simplex de 2 dimensões

from sympy import symbols

x1, x2 = symbols("x1 x2")

f = (x1)*x1 - 49

def cf(x):
    return f.subs({x1:x[0], x2:x[1]})

def simplex(v1, v2, v3, e):
    k = 0
    while k < 100:
        #ordenação:
        
        if cf(v1) < cf(v2) and cf(v1) < cf(v3):
            xl = v1
            if cf(v2) < cf(v3):
                xs = v2
                xn = v3
            else:
                xs = v3
                xn = v2
        elif cf(v2) < cf(v1) and cf(v2) < cf(v3):
            xl = v2
            if cf(v1) < cf(v3):
                xs = v1
                xn = v3
            else:
                xs = v3
                xn = v1
        elif cf(v3) < cf(v1) and cf(v3) < cf(v2):
            xl = v3
            if cf(v1) < cf(v2):
                xs = v1
                xn = v2
            else:
                xs = v2
                xn = v1
        f1 = cf(xn) #primeiro pior ponto
        #calculo do centroide
        c = [0.5 * (xl[0] + xs[0]), 0.5 * (xl[1] + xs[1])]

        #Reflexão:
        xr = [c[0] + (c[0]-xn[0]), c[1] + (c[1]-xn[1])]
        
        if cf(xr) < cf(xs) and cf(xr) > cf(xl):
            xn = xr
            v1 = xl
            v2 = xs
            v3 = xn
        #Expansão:
        elif cf(xr) < cf(xs) and cf(xr) < cf (xl):
            xe = [c[0] + 2*(xr[0]-c[0]), c[1] + 2*(xr[1]-c[1])]
            if cf(xr) < cf(xe):
                xn = xr
            else:
                xn = xe
            v1 = xl
            v2 = xs
            v3 = xn
        #Contração
        else:
            xc = [c[0] + 0.5*(xn[0]-c[0]), c[1] + 0.5*(xn[1]-c[1])]
            if cf(xc) < cf(xn):
                xn = xc
                v1 = xl
                v2 = xs
                v3 = xn
            #Contração Encolhida
            else:
                xl = xl
                xs = [xl[0] + 0.5*(xs[0]-xl[0]), xl[1] + 0.5*(xs[1]-xl[1])]
                xn = [xl[0] + 0.5*(xn[0]-xl[0]), xl[1] + 0.5*(xn[1]-xl[1])]
                v1 = xl
                v2 = xs
                v3 = xn
        f2 = cf(xl) #melhor ponto ao final da iteração
        
        if abs(f2 - f1) < e:
            break
        k = k+1
        print(xl)
        
    
    print(k)
    return xl
    
v1 = [0,0]
v2 = [2,2]
v3 = [4,4]

a = simplex(v1, v2, v3, 1e-10)
r = f.subs({x1:a[0], x2:a[1]})

print(a)
print(r)