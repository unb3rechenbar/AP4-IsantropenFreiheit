import math
from mathsfun import *

def txtRead(path):
    data = []
    units = []
    def Tupelblock(string):
        # Sammle die Einträge des Strings als Liste. Wenns leer ist, nimm halt Pi.
        Eintraege = [x.replace("\n","") if x.replace("\n","") != '' else str(math.pi) for x in string.split("\t")]
        
        # Füge die Einheiten zu den Einträgen als Tupel hinzu.
        return [(float(x.replace(",",".")), units[i]) if i in range(len(units)) else (float(x.replace(",",".")), "???") for i,x in enumerate(Eintraege)]
    
    # Teile den String in Zeilen auf.
    with open(path) as f:
        lines = f.readlines()
    
    # Verarbeite iterativ die Zeilen zu Werttupeln
    for i,l in enumerate(lines):
        if i == 0:
            # Für die erste Zeile lese Einheiten aus und entferne Zeilenumbruch, speichere als Tupel in "units" ab, um im Folgeschritt abrufbar zu sein
            units = [x.split(" / ")[1].replace("\n","") if 1 in range(len(x.split(" / "))) else "" for x in l.split("\t")]   
        elif i == len(lines):
            continue
        else:
            # Füge die Tupelblöcke zu "data" hinzu
            data.append(Tupelblock(l))
            
    return data

def cRead(path):
    data = []
    line = []
    units = []
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    with open(path) as f:
        lines = f.readlines()
    
    for i,l in enumerate(lines):
        if "#" in l:
            continue
        elif any(x in l for x in Alphabet):
            units = []
            for w in l.split(" "):
                units += [w.replace("\n","")]
        else:
            for i,w in enumerate(l.split(" ")):
                line += [Werttupel(float(w.replace("\n","")),units[i])]
            data += [line]
            line = []
            
    return data
        