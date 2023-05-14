from sys import path
path.append('Header')

from physicsfun import *
from readfun import *
from plotfun import *

# INFOCENTER
# -> Beim Graphen war "Grafik glätten" eingeschaltet
# -> 

# ========================================
# Vorbereitung: Festlegen der Reihenfolge
# 1. Random Übungsmessung Punkt 8
# 2. Temperaturmessung 73 Grad
# 3. Temperaturmessung 68 Grad
# 4. Temperaturmessung 63 Grad
# 5. Temperaturmessung 58 Grad
# 6. Temperaturmessung 53 Grad
# 7. Temperaturmessung 38 Grad
# 8. Temperaturmessung 31 Grad
# 9. Temperaturmessung 15 Grad
# 10. Temperaturmessung 10 Grad
# 11. Temperaturmessung 4 Grad
# 12. Temperaturmessung 0 Grad

# => Total 12 Messungen, card(I) = 12

# ========================================
# Vorbereitung: Einlesen der Daten
DatenUmgebung = cRead("../MessungenFreiheit/teil6.dat")
mDatenUmgebung = cRead("../MessungenFreiheit/teil6_cursormaxima.dat")
DatenRohr = cRead("../MessungenFreiheit/teil8.dat")
mDatenRohr = cRead("../MessungenFreiheit/teil8_cursormaxima.dat")

Rohrlaenge = Werttupel(1,"m")
KirchhoffK = Werttupel(0.0004,"m*(1/(sqrt(s)))")
RohrRadius = mal(0.5,plus(Werttupel(18.5,"mm"),neg(Werttupel(3,"mm"))))
KonstTemp = Werttupel(300,"K")
MolMasseCO2 = Werttupel(44.01,"g/mol")

# ========================================
# Vorbereitung: Zusammenfassen der Temperaturmessungen
Temperaturmessungen = [
    DatenRohr,
    cRead("../MessungenFreiheit/teil10/73.dat"),
    cRead("../MessungenFreiheit/teil10/68.dat"),
    cRead("../MessungenFreiheit/teil10/63.dat"),
    cRead("../MessungenFreiheit/teil10/58.dat"),
    cRead("../MessungenFreiheit/teil10/53.dat"),
    cRead("../MessungenFreiheit/teil10/38.dat"),
    cRead("../MessungenFreiheit/teil10/31.dat"),
    cRead("../MessungenFreiheit/teil10/15.dat"),
    cRead("../MessungenFreiheit/teil10/10.dat"),
    cRead("../MessungenFreiheit/teil10/4.dat"),
    cRead("../MessungenFreiheit/teil10/0.dat")
]

print(len(Temperaturmessungen))


# ========================================
# Vorbereitung: Händisches Ablesen der Maxima

Maxima = [
    [
        mDatenRohr[0][0],
        mDatenRohr[3][0],
        mDatenRohr[4][0],
        mDatenRohr[6][0],
        mDatenRohr[8][0],
        mDatenRohr[9][0],
        mDatenRohr[11][0],
        mDatenRohr[13][0]
    ],
    [
        10.6,
        146.1,
        290.1,
        430.1,
        575.3,
        716.7,
        859.3,
        998.7
    ],
    [
        11.2,
        146.8,
        288.8,
        428.8,
        542.8,
        712.8,
        856,
        997
    ],
    [
        11,
        145,
        287,
        426,
        566,
        768,
        854,
        987
    ],
    [
        12,
        143,
        286,
        426,
        563,
        703,
        844,
        980
    ],
    [
        11,
        142,
        283,
        420,
        580,
        698,
        838,
        976
    ],
    [
        8.7,
        139,
        277,
        413,
        550,
        688,
        824,
        960
    ],
    [
        11,
        142,
        275,
        412,
        550,
        685,
        821,
        955
    ],
    [
        10,
        137,
        267,
        399,
        532,
        663,
        797,
        931
    ],
    [
        8,
        134,
        263,
        394,
        528,
        656,
        785,
        914
    ],
    [
        8,
        134,
        263,
        393,
        523,
        649,
        781,
        909
    ],
    [
        10.6,
        133,
        282,
        390,
        521,
        647,
        776,
        907
    ]
]


# Aufgabe 1



# Aufgabe 2
# Kugelradius = 10
# MaximaFrequenzen = [
#     x.Wert if all(abs(x.Wert - y) > Kugelradius for y in [z.Wert for z in Spaltenauswahl(mDatenUmgebung,0)]) else None for x in Spaltenauswahl(mDatenRohr,0)
# ]

print([x.Wert for x in Spaltenauswahl(mDatenRohr,0)])

def Auswertungsprogramm(Daten):
    """Auswertungsprogramm

    Args:
        Daten (list): Enthält Datenpaar (WertelisteX, WertelisteY, MaximalisteX)
    """
    
    print([Daten[0],Daten[0]])
    
    StandardPGFPlot(
        [Daten[0],Daten[0]],
        [Daten[1],Daten[2]],
        [0 for y in Daten[0]],
        [[0 for y in Daten[1]]],
        [0],
        ["Frequenz","Dezibel - Volt"],
        "Umgebung",
        "Umgebungsmessung",
        [1,0]
    )


for i,x in enumerate(Maxima):
    # print(x)
    # print(WertSpaltenauswahl(Temperaturmessungen[i],0))
    # print(WertSpaltenauswahl(Temperaturmessungen[i],1))
    
    X = Spaltenauswahl(Temperaturmessungen[i],0)
    Y = Spaltenauswahl(Temperaturmessungen[i],1)
    
    Auswertungsprogramm((X,Y,x))

exit()


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

