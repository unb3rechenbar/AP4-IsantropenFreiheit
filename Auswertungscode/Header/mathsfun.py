import numpy as np
import math 


# Werttupel Implementierung und Grundfunktionen
class Werttupel:
    def __init__(self,Wert,Einheit):
        self.Wert = Wert
        self.Einheit = Einheit
    def __str__(self) -> str:
        return str(self.Wert) + " " + self.Einheit

def uprint(uw: list) -> str:
    return str(uw[0]) + " ± " + str(uw[1])

def Wertleser(l: list or tuple or Werttupel) -> str or list:
    if type(l) == Werttupel:
        return l.Wert
    else:
        return [x.Wert if type(x) == Werttupel else Wertleser(x) for x in l]


def Einheitenmagie(x: Werttupel):
    if x.Einheit == "m*1/s":
        x.Einheit = "m/s"
    elif x.Einheit == "(deg*1/(deg)^2)^2":
        x.Einheit = "(1/deg)^2"
    elif x.Einheit == "mV*hPa/mV":
        x.Einheit = "hPa"
    elif x.Einheit == "mV*m^3/mV":
        x.Einheit = "m^3"
    elif x.Einheit == "hPa*m^3*(1/(J/(mol*K)*K))":
        x.Einheit = "mol"
        x.Wert *= 100
    elif x.Einheit == "mV*hPa/mV":
        x.Einheit = "hPa"
    elif x.Einheit == "mV*m^3/mV":
        x.Einheit = "m^3"
    elif x.Einheit == "J/(mol*K)*K":
        x.Einheit = "J/mol"
    elif x.Einheit == "(1/(J/mol))":
        x.Einheit = "mol/J"
    elif x.Einheit == "hPa/mV*hPa":
        x.Einheit = "1/mV"
    elif x.Einheit == "hPa*m^3*(1/(J/(mol*K)*(K)^2))*K":
        x.Einheit = "mol"
        x.Wert *= 100
    elif x.Einheit == "hPa*mol/J*m^3/mV*mV":
        x.Einheit = "mol"
        x.Wert *= 100
    elif x.Einheit == "m^3*mol/J*hPa/mV*mV": 
        x.Einheit= "mol"
        x.Wert *= 100
    elif x.Einheit == "sqrt((mol)^2)":
        x.Einheit = "mol"
    elif x.Einheit == "hPa*m^3*mol/J":
        x.Einheit = "mol"
        x.Wert *= 100
    elif x.Einheit == "s*V*A":
        x.Einheit = "J"
    elif x.Einheit == "mol*J/(mol*K)*K*ln(m^3*(1/(m^3)))":
        x.Einheit = "J"
    elif (x.Einheit == "kg*m/s^2*(1/((mm)^2))") or (x.Einheit == "m/s^2*(1/((mm)^2))*kg") or (x.Einheit == "kg*(1/((mm)^2))*m/s^2") or (x.Einheit == "kg*m/s^2*(1/(mm*(mm)^2))*mm"):
        x.Einheit = "Pa"
        x.Wert = x.Wert/(10 ** 6)
    elif x.Einheit == "hPa":
        x.Einheit = "Pa"
        x.Wert = x.Wert * 100
    elif x.Einheit == "m*(1/(sqrt(s)))*(1/(mm*sqrt(Hz)))":
        x.Einheit = ""
        x.Wert *= 1000
    elif x.Einheit == "((1/()))^2*(1/(J/(mol*K)*K*(1/(g/mol))))*(Hz*m)^2":
        x.Einheit = ""
        x.Wert *= 0.001
    else: pass
    return x

# Vektorrichtungen
def Dimension(x: list) -> int:
    Dimensionen = [1 if isinstance(y,(int,float,Werttupel)) else Dimension(y) for y in x]
    return sum(Dimensionen)

def Dimensionsstruktur(x: list) -> list:
    Struktur = []
    for y in x:
        if isinstance(y,(int,float,Werttupel)):
            Struktur += [1]
        else:
            Struktur += [len(Dimensionsstruktur(y)) if all(type(z) == (int or float or Werttupel) for z in y) else Dimensionsstruktur(y)]
    return Struktur

def Richtungsabzähler(x: tuple or list) -> list:
    Abzählliste = []
    def Entpacker(x):
        Entpackt = [] 
        if isinstance(x,(int,float,Werttupel)):
            Entpackt.append(x)
        else:
            for y in x:
                Entpackt += Entpacker(y)
        return Entpackt
    for y in x:
        if isinstance(x,(int,float,Werttupel)):
            Abzählliste.append(y)
        else:
            Abzählliste += Entpacker(y)
    return Abzählliste

def Richtungsgenerator(Einträge: list or tuple, Längen: list or tuple) -> list:
    print("Erhalte die Eingabe " + str(Einträge) + "als Einträge ...")
    print("Erhalte die Eingabe " + str(Längen) + " als Vektoreintragsdimensionen ...")
    print("Der Ausgabevektor wird die Dimension " + str(Dimension(Längen)) + " haben ...")
    print("Es gibt genau " + str(len(Einträge)) + " Einträge ...")
    print("Starte Zerlegung ...")
    def Vektor(i: int,x: int, Bereich: list or tuple):
        # Erzeuge Vektor aus Eintagsbereich vom aktuellen Ort bis zum um die Länge des aktuellen Längeneintrags verschobenen Ortes
        print("Erzeuge Vektor Nr. " + str(i) + "...")
        print("Schneide Vektor aus Eintragsbereich von " + str(int(pNorm(Längen[0:i],1))) + " bis " + str(int(pNorm(Längen[0:i],1)) + x) + "...")
        print("Ergebnis des Vektors: " + str(Bereich[int(pNorm(Längen[0:i],1)) : int(pNorm(Längen[0:i],1)) + x]) + "...")
        print("Gebe Vektor an Zerleger zurück...")
        return Bereich[int(pNorm(Längen[0:i],1)) : int(pNorm(Längen[0:i],1)) + x]
    def Zerleger(E,L):
        # Zerlege den Eintragsbereich des Umfangs der Gesamtlänge des aktuellen Längeneintrags in Vektoren der Länge des aktuellen Längeneintrags
        print("Zerleger hat Anweisung empfangen...")
        return [Vektor(i,x,E) if type(x) == int else Zerleger(Vektor(i,ipNorm(x,1),E),x) for i,x in enumerate(L)]
    
    if len(Einträge) != pNorm(Längen,1):
        print("Es gibt nicht so viele Stellen wie Einträge!")
        exit()
    else:
        print("Die if Abfrage wurde durchlaufen, die Zerlegung kann beginnen ...")
        Ergebnis = Zerleger(Einträge,Längen)
        print("Zerlegung abgeschlossen, Ausgabe des Ergebnisses an Oberprogramm ...")
        
        return Ergebnis


def Einheitleser(x: list or tuple or Werttupel) -> str:
    lx = Richtungsabzähler(x)
    Einheit = ""
    if (all(type(y) == Werttupel for y in x) and (all(x[0].Einheit == y.Einheit for y in x))):
        Einheit = x[0].Einheit
        return Einheit
    elif all(type(y) == Werttupel for y in x):
        print("Die Einheiten der Einträge sind nicht gleich!")
        exit()
    else:
        print("Das Tupel enthält nicht nur Werttupel!")
        exit()

def Nulltupel(Länge) -> list:
    return [0 for i in range(Länge)]
def Einstupel(Länge) -> list:
    return [1 for i in range(Länge)]
def cTupel(Dimensionsstruktur: list,Wertliste: list) -> list:
    return Richtungsgenerator(Wertliste,Dimensionsstruktur)
def IndikatorTupel(Index: int,Länge: int) -> list:
    return [1 if i == Index else 0 for i in range(Länge)]
    
def R1RIdentifikator(l: list) -> list:
    return [x[0] if isinstance(x[0],(int,float,Werttupel)) else R1RIdentifikator(x)for x in l]
    
def pNorm(x: list or tuple or int or float,p: int or float) -> int or float:
    if type(x) == (int or float):
        return abs(x)
    else:
        return sum([e ** p if (type(e) == int or type(e) == float) else pNorm(e,p) for e in x]) ** (1/p)

def ipNorm(x: list,p: int or float) -> int:
    return int(pNorm(x,p))

def maxNorm(x: list or tuple or int) -> int or float:
    return max([abs(e) if not (isinstance(e,list) or isinstance(e,tuple)) else maxNorm((e)) for e in x])

def WinkelnachRad(x: int or float) -> float:
    return x * math.pi / 180

# SCHWELLENBESTIMMUNG
def Schwellenbrecher(Werte: list,Trigger: int or float) -> int or float:
    for x in Werte:
        if x > Trigger:
            return x
    return None
def WertSchwellenbrecher(WListe: list,Trigger: int or float) -> Werttupel:
    for x in WListe:
        if x.Wert > Trigger:
            return x
    return None

# NULLSTELLEN
def GeradenAbschnitt(Steigung: int or float,Graphenpunkt: tuple) -> int or float:
    return Graphenpunkt[1] - Steigung * Graphenpunkt[0]
def GeradenNullstelle(Steigung: int or float,Abschnitt: int or float) -> int or float:
    return -Abschnitt/Steigung
def dGeradenNullstelle(SteigunguF: tuple,AbschnittuF: tuple,r: int,h: tuple):
    if r == 1:
        return AbschnittuF[0] / (SteigunguF[0] ** 2)
    elif r == 2:
        return -1 / SteigunguF[0]
    else: 
        return "Nicht zulässige Ableitungsrichtung!"

# W - SKALAR FUNKTIONEN
def smal(s: int or float,W: Werttupel):
    return Werttupel(s * W.Wert,W.Einheit)

# GRÜSSE AN JUNK: Grundfunktionen auf Werttupel erweitert
def mal(W1: int or float or Werttupel,W2: int or float or Werttupel) -> int or float or Werttupel:
    if (isinstance(W1,(int,float)) and isinstance(W2,(int,float))):
        return W1 * W2
    elif (isinstance(W1,(int,float)) and isinstance(W2,(Werttupel))):
        return smal(W1,W2)
    elif (isinstance(W1,(Werttupel)) and isinstance(W2,(int,float))):
        return smal(W2,W1)
    else:
        unit = W1.Einheit + "*" + W2.Einheit if W1.Einheit and W2.Einheit else W1.Einheit or W2.Einheit
        return Werttupel(W1.Wert * W2.Wert,unit)

def plus(W1: int or float or Werttupel,W2: int or float or Werttupel) -> int or float or Werttupel:
    if (isinstance(W1,(int,float)) and isinstance(W2,(int,float))):
        return W1 + W2
    elif (isinstance(W1,(Werttupel)) and isinstance(W2,(Werttupel))):
        if W1.Einheit == W2.Einheit:
            return Werttupel(W1.Wert + W2.Wert,W1.Einheit)
        else: 
            print("Einheiten in plus-Auswertung sind nicht gleich!") 
            exit(1)
    elif (isinstance(W1,(int,float)) and isinstance(W2,(Werttupel))):
        if W2.Einheit == "":
            return Werttupel(W1 + W2.Wert,W2.Einheit)
        else:
            print("Skalar und Werttupel sind nicht addierbar!")
            exit(1)
    else:
        if W1.Einheit == "":
            return Werttupel(W1.Wert + W2,W1.Einheit)
        else:
            print("Skalar und Werttupel sind nicht addierbar!")
            exit(1)

def wsum(W1: list) -> int or float or Werttupel:
    if all(isinstance(x,(int,float)) for x in W1):
        return sum(W1)
    elif all(isinstance(x,(Werttupel)) for x in W1):
        Summe = Werttupel(0,Einheitleser(W1))
        for x in W1:
            Summe = plus(Summe,x)
        return Summe
    else:
        print("Werttupel und Skalare sind nicht addierbar!")
        exit(1)
        
def inv(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return 1 / W
    else:
        return Werttupel(1 / W.Wert,"(1/(" + W.Einheit + "))")
    
def neg(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return -W
    else:
        return Werttupel(-W.Wert,W.Einheit)

def wabs(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return abs(W)
    else:
        return Werttupel(abs(W.Wert),W.Einheit)

def sgn(W: int or float or Werttupel) -> int:
    x = W if isinstance(W,(int,float)) else W.Wert
    return 1 if x >= 0 else -1


# GRÜSSE AN JUNK: REELLE ZAHLEN
def Ker(x: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(x,(int,float)):
        return inv(x) if x != 0 else 0
    else:
        return inv(x) if x.Wert != 0 else Werttupel(0,x.Einheit)
  
# GRÜSSE AN JUNK: Tupel
def pmal(T1: tuple or list,T2: tuple or list) -> list:
    bT1 = Richtungsabzähler(T1)
    bT2 = Richtungsabzähler(T2)
    
    if len(bT1) != len(bT2):
        print("Tupel in pmal-Auswertung haben nicht dieselbe Anzahl an Elementen!")
        exit()
    else:
        Produkt = [mal(x,y) for (x,y) in zip(bT1,bT2)]
    return Richtungsgenerator(Produkt,Dimensionsstruktur(T1))

def stupelmal(Skalar: int or float or Werttupel,Tupel: tuple or list) -> list:
    return [mal(Skalar,x) for x in Tupel]


# Ableitungen der Grundfunktionen
def dinv(W: Werttupel):
    if W.Wert == 0:
        return Werttupel(0,"1/" + W.Einheit)
    else:  
        return Werttupel(-W.Wert ** -2,"1/" + W.Einheit + "^2")


# einfache Funktionsverkettungen der Grundfunktionen
def wurzel(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return np.sqrt(W)
    else:
        return Werttupel(np.sqrt(W.Wert),"sqrt(" + W.Einheit + ")")

def quadrat(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return W ** 2
    else:
        return Werttupel(W.Wert ** 2,"(" + W.Einheit + ")^2")


# Spezielle Grundfunktionsverkettungen
def wsin(W: int or float or Werttupel) -> int or float or Werttupel:
    if isinstance(W,(int,float)):
        return np.sin(W)
    else:
        return Werttupel(np.sin(W.Wert),"")

def wcos(W: int or float or Werttupel) -> int or float or Werttupel:
    return np.cos(W) if isinstance(W,(int,float)) else Werttupel(np.cos(W.Wert),"")

def scpr(W1: int or float or Werttupel or list or tuple, W2: int or float or Werttupel or list or tuple) -> int or float or Werttupel:
    if (isinstance(W1,(int,float,Werttupel))) and (isinstance(W2,(int,float,Werttupel))):
        print(Einheitenmagie(mal(W1,W2)))
        return Einheitenmagie(mal(W1,W2))
    elif (isinstance(W1,(list,tuple)) and isinstance(W2,(list,tuple))):
        if Dimensionsstruktur(W1) == Dimensionsstruktur(W2):
            return wsum([scpr(x,y) for (x,y) in zip(W1,W2)])
        else:
            print("Dimensionsstrukturen stimmen nicht überein!")
            exit(1)
    else:
        print("Werte in scpr-Auswertung sind nicht kompatibel!")
        exit(1)

# Unsicherheitsberechnung
def wUnsicherheit(f: tuple,x: tuple,ux: tuple) -> tuple:
    Unsicherheitquadratsummanden = []
    for i in range(Dimension(x)):
        print("Starte...")
        print(Richtungsgenerator(
                    [Richtungsabzähler(ux)[j] if j == 3 else Werttupel(0,"") for j in range(Dimension(x))],
                    Dimensionsstruktur(x)
                ))
        dfWert = f[1](
            *x,
            R1RIdentifikator(
                Richtungsgenerator(
                    [Richtungsabzähler(ux)[j] if j == 3 else Werttupel(0,"") for j in range(Dimension(x))],
                    Dimensionsstruktur(x)
                )
            )
        )
        print("Hat geklappt...")
        print(dfWert)
        Unsicherheitquadratsummanden.append(quadrat(dfWert))
    
    Unsicherheit = Unsicherheitquadratsummanden[0]
    for u in Unsicherheitquadratsummanden[1:]:
        Unsicherheit = plus(Unsicherheit,u)
        
    return (f[0](*x),wurzel(Unsicherheit))

        
# Pauschale Unsicherheiten
def uPauschal(x: int or float or Werttupel or list) -> int or float or Werttupel:
    if isinstance(x,(int,float,Werttupel)):
        return mal(0.1,x)
    else:
        return stupelmal(0.1,x)
