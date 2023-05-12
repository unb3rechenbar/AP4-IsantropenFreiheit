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

print([x.Wert for x in mDatenRohr])

MaximaFrequenzen = [
    mDatenRohr[0]
]