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

Reihenfolge = [
    "ÜbungsMessung",
    "Temperaturmessung 73 Grad",
    "Temperaturmessung 68 Grad",
    "Temperaturmessung 63 Grad",
    "Temperaturmessung 58 Grad",
    "Temperaturmessung 53 Grad",
    "Temperaturmessung 38 Grad",
    "Temperaturmessung 31 Grad",
    "Temperaturmessung 15 Grad",
    "Temperaturmessung 10 Grad",
    "Temperaturmessung 4 Grad",
    "Temperaturmessung 0 Grad"
]
Temperaturen = [math.pi,73,68,63,58,53,38,31,15,10,4,0]

# ========================================
# Vorbereitung: Festlegen des Speicherortes
Dateipfad = "../Versuchsbericht/Sektionen/AuswertungsergebnisseFreiheit/"

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

uMaxList = [
    Werttupel(5,"Hz") for x in Maxima[0]
]

# ========================================
# Vorbereitung: Umwandeln der Maxima in Werttupel
for x in Maxima:
    for y in x:
        if isinstance(y, Werttupel):
            continue
        else:
            x[x.index(y)] = Werttupel(y,"Hz")


# ========================================
# Auswertung: Definition des Auswertungsprogramms

def Auswertungsprogramm(Daten,i):
    """Auswertungsprogramm

    Args:
        Daten (list): Enthält Datenpaar (WertelisteX, WertelisteY, MaximalisteX)
    """
    
    # Aufgabe 1
    with open(Dateipfad + "Graphen/" + Reihenfolge[i] + ".tex","w") as graphfile:
        fileStandardPGFPlot(
            [Daten[0]],
            [Daten[1]],
            [0 for y in Daten[0]],
            [[0 for y in Daten[1]]],
            [0],
            ["Frequenz","Dezibel - Volt"],
            "Umgebung",
            "Umgebungsmessung",
            [1,0],
            graphfile
        )
    
    # Aufgabe 2
    Schallgeschwindigkeiten = [
        SchallRohr(i + 1,x,Rohrlaenge) for i,x in enumerate(MaxList)
    ]
    uSchallgeschwindigkeiten = [
        wUnsicherheit(
            (SchallRohr,dSchallRohr),
            (i + 1,x,Rohrlaenge),
            (0,uMaxList[i],Werttupel(1,"cm"))
        )[1] for i,x in enumerate(MaxList)
    ]
    
    exit()
    
    # Aufgabe 3
    Korrekturen = [
        SchallKorrektur(KirchhoffK,RohrRadius,x,Schallgeschwindigkeiten[i]) for i,x in enumerate(MaxList)
    ]
    uKorrekturen = uPauschal(Korrekturen)
    
    # Aufgabe 4
    Kappas = [
        invSchallKorrektur(KirchhoffK,RohrRadius,x,KonstTemp,MolMasseCO2,Korrekturen[i]) for i,x in enumerate(MaxList)
    ]
    uKappas = uPauschal(Kappas)
    
    Freiheiten = [
        Freiheit(k) for k in Kappas
    ]
    uFreiheiten = uPauschal(Freiheiten)
    
    # Zusammenfassen
    uMMaxList = mal(wurzel(wsum([quadrat(x) for x in uMaxList])),inv(len(uMaxList)))
    uMSchall = mal(wurzel(wsum([quadrat(x) for x in uSchallgeschwindigkeiten])),inv(len(uSchallgeschwindigkeiten)))
    uMKorrektur = mal(wurzel(wsum([quadrat(x) for x in uKorrekturen])),inv(len(uKorrekturen)))
    uMKappa = mal(wurzel(wsum([quadrat(x) for x in uKappas])),inv(len(uKappas)))
    uMFreiheit = mal(wurzel(wsum([quadrat(x) for x in uFreiheiten])),inv(len(uFreiheiten)))
    
    with open(Dateipfad + "Tabellen/" + Reihenfolge[i] + ".tex","w") as tablefile:
        fileLatexTabelle(
            ["$\\nu$","c","C(c)","$\\kappa$","f"],
            [
                [
                    i,
                    [MaxList[i],uMaxList[i]],
                    [Schallgeschwindigkeiten[i],uSchallgeschwindigkeiten[i]],
                    [Korrekturen[i],uKorrekturen[i]],
                    [Kappas[i],uKappas[i]],
                    [Freiheiten[i],uFreiheiten[i]]
                ] for i in range(len(MaxList))
            ] + [[[0,0],
                [mal(wsum(MaxList),inv(len(MaxList))),uMMaxList],
                [mal(wsum(Schallgeschwindigkeiten),inv(len(Schallgeschwindigkeiten))),uMSchall],
                [mal(wsum(Korrekturen),inv(len(Korrekturen))),uMKorrektur],
                [mal(wsum(Kappas),inv(len(Kappas))),uMKappa],
                [mal(wsum(Freiheiten),inv(len(Freiheiten))),uMFreiheit]
            ]],
            tablefile
        )
        
    # Speichern der Kappas und Freiheitsgrade
    KappaSammlung.append(mal(wsum(Kappas),inv(len(Kappas))))
    FreiheitSammlung.append(mal(wsum(Freiheiten),inv(len(Freiheiten))))
    

# ========================================
# Auswertung: Abruf des Auswertungsprogramms für alle Messungen

KappaSammlung = []
FreiheitSammlung = []

for i,MaxList in enumerate(Maxima):
    print("Auswertung der Messung '" + Reihenfolge[i] + "'...")
    
    X = Spaltenauswahl(Temperaturmessungen[i],0)
    Y = Spaltenauswahl(Temperaturmessungen[i],1)

    Auswertungsprogramm((X,Y,MaxList),i)
        

with open(Dateipfad + "KappaTemperatur.tex","w") as file:
    fileStandardPGFPlot(
        [Temperaturen],
        [KappaSammlung],
        [0 for x in Temperaturen],
        [Wertleser(uPauschal(KappaSammlung))],
        [0],
        ["Temperatur","Kappa"],
        "$\\kappa(T)$",
        "KappaTemperatur",
        [1,0],
        file
    )
    
with open(Dateipfad + "FreiheitTemperatur.tex","w") as file:
    fileStandardPGFPlot(
        [Temperaturen],
        [FreiheitSammlung],
        [0 for x in Temperaturen],
        [Wertleser(uPauschal(FreiheitSammlung))],
        [0],
        ["Temperatur","Freiheit"],
        "$f(T)$",
        "FreiheitTemperatur",
        [1,0],
        file
    )