from sys import path
path.append('Header')

from physicsfun import *
from readfun import *
from plotfun import *

# INFOCENTER
# -> Beim Graphen war "Grafik glätten" eingeschaltet
# -> 

# Aufgabe 1
DatenUmgebung = cRead("../MessungenFreiheit/teil6.dat")
mDatenUmgebung = cRead("../MessungenFreiheit/teil6_cursormaxima.dat")
DatenRohr = cRead("../MessungenFreiheit/teil8.dat")
mDatenRohr = cRead("../MessungenFreiheit/teil8_cursormaxima.dat")

Rohrlaenge = Werttupel(1,"m")
KirchhoffK = Werttupel(0.0004,"m*(1/(sqrt(s)))")
RohrRadius = mal(0.5,plus(Werttupel(18.5,"mm"),neg(Werttupel(3,"mm"))))
KonstTemp = Werttupel(300,"K")
MolMasseCO2 = Werttupel(44.01,"g/mol")

StandardPGFPlot(
    [[x.Wert for x in Spaltenauswahl(DatenUmgebung,0)],[x.Wert for x in Spaltenauswahl(mDatenUmgebung,0)]],
    [[y.Wert for y in Spaltenauswahl(DatenUmgebung,1)],[y.Wert for y in Spaltenauswahl(mDatenUmgebung,1)]],
    [0 for x in Spaltenauswahl(DatenUmgebung,0)],
    [[0 for y in Spaltenauswahl(DatenUmgebung,1)], [0 for y in Spaltenauswahl(mDatenUmgebung,1)]],
    [0,0],
    ["Frequenz","Dezibel - Volt"],
    "Umgebung",
    "Umgebungsmessung",
    [1,0]
)

# Aufgabe 2
# Kugelradius = 10
# MaximaFrequenzen = [
#     x.Wert if all(abs(x.Wert - y) > Kugelradius for y in [z.Wert for z in Spaltenauswahl(mDatenUmgebung,0)]) else None for x in Spaltenauswahl(mDatenRohr,0)
# ]

print([x.Wert for x in Spaltenauswahl(mDatenRohr,0)])

MaximaFrequenzen = [
    mDatenRohr[0][0],
    mDatenRohr[3][0],
    mDatenRohr[4][0],
    mDatenRohr[6][0],
    mDatenRohr[8][0],
    mDatenRohr[9][0],
    mDatenRohr[11][0],
    mDatenRohr[13][0]
]
print([x.Wert for x in MaximaFrequenzen])

Schallgeschwindigkeiten = [
    SchallRohr(i + 1,x,Rohrlaenge) for i,x in enumerate(MaximaFrequenzen)
]
print([x.Wert for x in Schallgeschwindigkeiten])


# Aufgabe 3
Korrekturen = [
    SchallKorrektur(KirchhoffK,RohrRadius,x,Schallgeschwindigkeiten[i]) for i,x in enumerate(MaximaFrequenzen)
]
print([x.Wert for x in Korrekturen])

# Aufgabe 4
Kappas = [
    invSchallKorrektur(KirchhoffK,RohrRadius,x,KonstTemp,MolMasseCO2,Korrekturen[i]) for i,x in enumerate(MaximaFrequenzen)
]
print([x.Wert for x in Kappas])

Freiheiten = [
    Freiheit(k) for k in Kappas
]
print([x.Wert for x in Freiheiten])