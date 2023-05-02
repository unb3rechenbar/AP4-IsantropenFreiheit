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
    Gradient += [1] # Ableitung nach p0
    Gradient += [mal(g,inv(mal(math.pi,quadrat(r))))] # Ableitung nach mS
    Gradient += [mal(mS,inv(mal(math.pi,quadrat(r))))] # Ableitung nach g
    Gradient += [mal(mal(mal(mS,g),inv(math.pi)),mal(-2,inv(mal(r,quadrat(r)))))] # Ableitung nach r
    
    # print(Gradient[1])
    
    return scpr(Gradient,h)