from sys import path
path.append('Header')

from physicsfun import *

# --- Einlesen der Messdaten ---
# Tupel mit (Schwingzahl,Schwingdauer)
RueckFlammAr = cRead("../MessungenIso/Schwingungsmessungen.txt")[0] 
RueckFlammCO2 = cRead("../MessungenIso/Schwingungsmessungen.txt")[1]
RueckFlammN2 = cRead("../MessungenIso/Schwingungsmessungen.txt")[2]
# FRAGE: Ist die Zuordnung richtig?

HoehenAg = cRead("../MessungenIso/Hoehenmessungen.txt")[0:2]
HoehenCO2 = cRead("../MessungenIso/Hoehenmessungen.txt")[2:4]
HoehenN2 = cRead("../MessungenIso/Hoehenmessungen.txt")[4:6]

print(HoehenCO2[1][3])

# --- Aufgabe 1 ---
Auussentemperatur = Werttupel(21,"deg")
Luftdruck = Werttupel(963.2,"hPa")
MasseSchwingkoerper = Werttupel(0.5,"kg") # Anpassen
Glasrohrradius = Werttupel(0.5,"mm") # Anpassen

EffektivesVolumen = [
    Werttupel(0.5,"l"),
    Werttupel(0.5,"l"),
    Werttupel(0.5,"l")    
] # Anpassen
Schwingdauer = [
    RueckFlammAr[1],
    RueckFlammCO2[1],
    RueckFlammN2[1] 
]

def Adiabateniteration(Veff: Werttupel, Ts: Werttupel):
    
    GleichgewichtsDruck = Gasdruck(
        Luftdruck,
        MasseSchwingkoerper,
        Erdbeschleunigung,
        Glasrohrradius
    )
    
    dGleichgewichtsDruck = dGasdruck(
        Luftdruck,
        MasseSchwingkoerper,
        Erdbeschleunigung,
        Glasrohrradius,
        [
            Werttupel(5,"hPa"),
            Werttupel(0.01,"kg"),
            Werttupel(0.01,"m/s^2"),
            Werttupel(0.1,"mm")
        ]
    )

    Kappa = Kappa1(
        MasseSchwingkoerper,
        Veff,
        Ts,
        GleichgewichtsDruck,
        Glasrohrradius
    )

    # dKappa = dKappa1(
    #     MasseSchwingkoerper,
    #     Veff,
    #     Ts,
    #     GleichgewichtsDruck,
    #     Glasrohrradius,
    #     [
    #         Werttupel(0.01,"kg"),
    #         uPauschal(Veff),
    #         uPauschal(Ts),
    #         dGleichgewichtsDruck,
    #         Werttupel(0.1,"mm")
    #     ]
    # )
    # exit()
    
    dKappa = uPauschal(Kappa)
    
    return (Kappa,dKappa)
    
# --- Iteration ---
Namen = ["Argon","Kohlenstoffdioxid","Stickstoff"]
for i in range(3):
    print("Der Adiabatenexponent für " + Namen[i] + " lautet " + str(Adiabateniteration(EffektivesVolumen[i],Schwingdauer[i])[0]) + " ± " + str(Adiabateniteration(EffektivesVolumen[i],Schwingdauer[i])[1]) + ".")
    
# --- Aufgabe 2 ---
Hoehenunsicherheit = Werttupel(3,"mm")

def Adiabateniteration(H: list):
    print(H[0][2])
    Hoehenmittel1 = mal(1 / 3,wsum(H[0][1:]))
    Hoehenmittel3 = mal(1 / 3,wsum(H[1][1:]))
    
    
    Kappa = Kappa2(
        Hoehenmittel1,
        Hoehenmittel3,
    )
    # dKappa = dKappa2(
    #     Hoehenmittel1,
    #     Hoehenmittel3,
    #     [
    #         Hoehenunsicherheit,
    #         Hoehenunsicherheit
    #     ]   
    # )
    
    dKappa = uPauschal(Kappa)
    
    return (Kappa,dKappa)

HoehenSammlung = [HoehenAg,HoehenCO2,HoehenN2]

for i in range(3):
    print("Der Adiabatenexponent für " + Namen[i] + " lautet " + str(Adiabateniteration(HoehenSammlung[i])[0]) + " ± " + str(Adiabateniteration(HoehenSammlung[i])[1]) + ".")
    