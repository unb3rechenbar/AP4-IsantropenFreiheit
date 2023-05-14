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
MasseSchwingkoerper = Werttupel(0.00987,"kg")
uMasseSchwingkoerper = Werttupel(0.0001,"kg")
Glasrohrradius = Werttupel(4.960,"mm") 
uGlasrohrradius = Werttupel(0.01,"mm") 

EffektivesVolumen = [
    (Werttupel(2182,"cm^3"),Werttupel(1, "cm^3")),
    (Werttupel(2182,"cm^3"),Werttupel(1, "cm^3")),
    (Werttupel(2182,"cm^3"),Werttupel(1, "cm^3")),    
] # Anpassen
Schwingdauer = [
    (mal(RueckFlammAr[1],1/300), Werttupel(1/300,"s")),
    (mal(RueckFlammCO2[1],1/300), Werttupel(1/300,"s")),
    (mal(RueckFlammN2[1],1/300),Werttupel(20/300,"s")) 
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
            uMasseSchwingkoerper,
            Werttupel(0.01,"m/s^2"),
            uGlasrohrradius
        ]
    )

    Kappa = Kappa1(
        MasseSchwingkoerper,
        Veff[0],
        Ts[0],
        GleichgewichtsDruck,
        Glasrohrradius
    )

    dKappa = dKappa1(
         MasseSchwingkoerper,
         Veff[0],
         Ts[0],
         GleichgewichtsDruck,
         Glasrohrradius,
        [
             Werttupel(0.01,"kg"),
             Veff[1],
             Ts[1],
             dGleichgewichtsDruck,
             uGlasrohrradius
         ]
    )
    # exit()
    
    # dKappa = uPauschal(Kappa)
    return (Kappa,dKappa)
    
# --- Iteration ---
Namen = ["Argon","Kohlenstoffdioxid","Stickstoff"]
MagischerSIFaktor = 10**6
for i in range(3):
    Exponent = Adiabateniteration(EffektivesVolumen[i],Schwingdauer[i])
    #print(Exponent)
    print("Der Adiabatenexponent für " + Namen[i] + " lautet " + str(mal(MagischerSIFaktor, Exponent[0]))
           + " ± " + str(mal(MagischerSIFaktor, Exponent[1])) + ".")
    
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
    