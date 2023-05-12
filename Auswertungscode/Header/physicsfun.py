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


# Aufgabe 2

# Aufgabe 3
def SchallKorrektur(a: Werttupel, r: Werttupel, v: Werttupel,c0: Werttupel):
    Bruch = mal(a,inv(mal(mal(2,r),wurzel(mal(math.pi,v)))))
    Klammer = plus(1,neg(mal(Bruch)))
    return mal(c0,Klammer)

def SchallFreierRaum(p: Werttupel, r: Werttupel, k: Werttupel):
    return wurzel(mal(mal(p,inv(r)),k))

def SchallRohr(n: Werttupel, f: Werttupel, L: Werttupel):
    return mal(mal(n,2),mal(f,L))

