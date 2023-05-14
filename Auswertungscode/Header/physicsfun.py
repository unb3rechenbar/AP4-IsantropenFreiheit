from mathsfun import *
from readfun import *
from plotfun import *
from variables import *


def Einheitenkuerzer(x: Werttupel):
    if x.Einheit == "m*1/s":
        x.Einheit = "m/s"
    if x.Einheit == "(deg*1/(deg)^2)^2":
        x.Einheit = "(1/deg)^2"
    if x.Einheit == "J*1/kg*(m/s)^2":
        x.Einheit = ""
    else: pass
    return x

def NanFilter(data):
    filtered = []
    for x in data:
        filtered.append(x) if not (math.isnan(x)) else None
    return filtered

# SPEZIELLE AP FUNKTIONEN
# alle Funktionen geben ein Tupel der Form (Wert,Unsicherheit) mit Werttupeln als Einträge zurück


def Kappa1(m: Werttupel, V: Werttupel, T: Werttupel, p: Werttupel, r: Werttupel):
    return mal(mal(4,mal(m,V)),inv(mal(quadrat(T),mal(p,quadrat(quadrat(r))))))

def dKappa1(m: Werttupel, V: Werttupel, T: Werttupel, p: Werttupel, r: Werttupel,h: list):
    Gradient = []
    Gradient += [mal(4,mal(V,inv(mal(quadrat(T),mal(p,quadrat(quadrat(r)))))))] # Ableitung nach m
    Gradient += [mal(4,mal(m,inv(mal(quadrat(T),mal(p,quadrat(quadrat(r)))))))] # Ableitung nach V
    Gradient += [mal(mal(4,mal(m,V)),mal(-2,inv(mal(mal(T,quadrat(T)),mal(p,quadrat(quadrat(r)))))))] # Ableitung nach T
    Gradient += [mal(mal(mal(4,mal(m,V)),inv(mal(quadrat(T),quadrat(quadrat(r))))),mal(-1,inv(quadrat(p))))] # Ableitung nach p  
    Gradient += [mal(mal(mal(4,mal(m,V)),inv(mal(quadrat(T),p))),mal(-4,inv(mal(r,quadrat(quadrat(r))))))] # Ableitung nach r

    for i in range(len(Gradient)):
        Gradient[i].Einheit = ""
        h[i].Einheit = ""
        Gradient[i] = quadrat(Gradient[i])
        h[i] = quadrat(h[i])

    return scpr(Gradient,h)

def Kappa2(dp1: Werttupel, dp3: Werttupel):
    return mal(dp1,inv(plus(dp1,neg(dp3))))
def dKappa2(dp1: Werttupel, dp3: Werttupel,h: list):
    Gradient = []
    Gradient += [plus(inv(plus(dp1,neg(dp3))),mal(dp1,mal(-1,inv(quadrat(plus(dp1,neg(dp3)))))))] # Ableitung nach dp1
    Gradient += [mal(dp1,mal(-1,inv(quadrat(plus(dp1,neg(dp3))))))] # Ableitung nach dp3

    return scpr(Gradient,h)

def Gasdruck(p0: Werttupel, mS: Werttupel, g: Werttupel, r: Werttupel):
    Ergebnis = Einheitenmagie(mal(mal(mS,g),inv(mal(math.pi,quadrat(r)))))
    return plus(Einheitenmagie(p0),Ergebnis)

def dGasdruck(p0: Werttupel, mS: Werttupel, g: Werttupel, r: Werttupel,h: list):
    Gradient = []
    Gradient += [Werttupel(1,"")] # Ableitung nach p0
    Gradient += [mal(g,inv(mal(math.pi,quadrat(r))))] # Ableitung nach mS
    Gradient += [mal(mS,inv(mal(math.pi,quadrat(r))))] # Ableitung nach g
    Gradient += [mal(mal(mal(mS,g),inv(math.pi)),mal(-2,inv(mal(r,quadrat(r)))))] # Ableitung nach r

    # print(Gradient[1])

    for i in range(len(Gradient)):
        Gradient[i].Einheit = ""
        h[i].Einheit = ""
        Gradient[i] = quadrat(Gradient[i])
        h[i] = quadrat(h[i])

    return scpr(Gradient,h) 

# Aufgabe 2

# Aufgabe 3
def SchallKorrektur(a: Werttupel, r: Werttupel, v: Werttupel,c0: Werttupel):
    Bruch = Einheitenmagie(mal(a,inv(mal(mal(2,r),wurzel(mal(math.pi,v))))))
    Klammer = plus(1,neg(Bruch))
    return mal(c0,inv(Klammer))

def dSchallKorrektur(a: Werttupel, r: Werttupel, v: Werttupel, c: Werttupel, h: list):
    da = mal(mal(mal(2,c),mal(r,wurzel(mal(math.pi,v)))),inv(quadrat(plus(a,neg(mal(2,mal(r,wurzel(mal(math.pi,v)))))))))
    dr = mal(mal(mal(-2,a),mal(c,wurzel(mal(math.pi,v)))),inv(quadrat(plus(mal(mal(2,wurzel(mal(math.pi,v))),r),neg(a)))))
    dc = mal(mal(2,mal(wurzel(mal(math.pi,v)),r)),inv(plus(mal(mal(2,wurzel(mal(math.pi,v))),r),neg(a))))
    dv = mal(mal(mal(-a,c),mal(r,wurzel(math.pi))),inv(mal(wurzel(v),quadrat(plus(mal(mal(2,wurzel(mal(math.pi,v))),r),neg(a))))))
    
    Gradient = [da,dr,dv,dc]
    return scpr(Gradient,h)

def SchallFreierRaum(p: Werttupel, r: Werttupel, k: Werttupel):
    return wurzel(mal(mal(p,inv(r)),k))

def SchallRohr(n: Werttupel, f: Werttupel, L: Werttupel):
    return mal(mal(inv(n),2),mal(f,L))

def dSchallRohr(n: Werttupel, f: Werttupel, L: Werttupel, h: list):
    df = mal(mal(inv(n),2),L)
    dL = mal(mal(inv(n),2),f)
    dn = mal(mal(mal(-1,inv(quadrat(n))),2),mal(f,L))
    
    Gradient = [dn,df,dL]
    return scpr(Gradient,h)

def invSchallKorrektur(a: Werttupel, r: Werttupel, v: Werttupel, T: Werttupel, M: Werttupel, c: Werttupel):
    Bruch = Einheitenmagie(mal(a,inv(mal(mal(2,r),wurzel(mal(math.pi,v))))))
    invBruch = inv(plus(1,neg(Bruch)))
    invBruch2 = inv(mal(mal(UniverselleGasKonstante,T),inv(M)))
    return Einheitenmagie(mal(mal(quadrat(invBruch),invBruch2),quadrat(c)))

def Freiheit(k: Werttupel):
    return mal(2,inv(plus(k,neg(1))))

def dFreiheit(k: Werttupel, h: list):
    dk = mal(-2,inv(quadrat(plus(k,neg(1)))))