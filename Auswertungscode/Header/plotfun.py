from mathsfun import *
import matplotlib.pyplot as plt

# GRUNDFUNKTIONEN
def ErsteSpalteAlsX(Daten):
    return [Wertleser(x[0]) for x in Daten]
def RestAlsY(Daten):
    return [[Wertleser(x[i + 1]) for x in Daten] for i in range(len(Daten[0]) - 1)]
def WertSpaltenauswahl(Daten,Spalte):
    return [Wertleser(x[Spalte]) for x in Daten]
def Spaltenauswahl(Daten,Spalte):
    return [x[Spalte] for x in Daten]


# PLOTTER UND VARIANTEN
def Scatter(X,YListe,Labels,Title,Trigger):
    if Trigger != 0:
        plt.figure(figsize=(8,4),dpi=100)
        axes = plt.axes()

        for i,y in enumerate(YListe):
            axes.scatter(X,y)

        axes.set_xlabel(Labels[0])
        axes.set_ylabel(Labels[1])
    
        axes.set_title(Title)

        plt.show()
    else:
        pass
    
def uScatter(X,YListe,Labels,Title,Trigger):
    if Trigger != 0:
        plt.figure(figsize=(8,4),dpi=100)
        axes = plt.axes()

        for Y in YListe:
            axes.scatter(
                [x.Wert for (x,u) in X],
                [y.Wert for (y,u) in Y],
            )
            axes.errorbar(
                [x.Wert for (x,u) in X],
                [y.Wert for (y,u) in Y], 
                xerr=[u.Wert for (x,u) in X], 
                yerr=[u.Wert for (y,u) in Y], 
                fmt='black', label='Fehler', ls='none')

        axes.set_xlabel(Labels[0])
        axes.set_ylabel(Labels[1])
    
        axes.set_title(Title)

        plt.show()
    else:
        pass


def Plotter(X,YListe,Labels,Title,Trigger):
    if Trigger != 0:
        plt.figure(figsize=(8,4),dpi=100)
        axes = plt.axes()

        for i,(x,y) in enumerate(zip(X,YListe)):
            if isinstance(X[0],Werttupel):
                axes.plot(
                    [z.Wert for z in x],
                    [z.Wert for z in y]
                )
            else:
                axes.plot(
                            [z.Wert for z in x],
                            [z.Wert for z in y]
                          )

        axes.set_xlabel(Labels[0])
        axes.set_ylabel(Labels[1])
    
        axes.set_title(Title)

        plt.show()
    else:
        pass


def StandardPGFPlot(
        X: list,
        Y: list,
        Xerror: list,
        Yerror: list,
        RegSetting: list,
        Labels: list,
        Caption: str,
        Label: str,
        Conf: list
    ):
    colors = ["red","blue","green","yellow","orange","brown","pink"]
    
    if Conf[0] != 0:
        def Tabellenblock(X,Y,Xerror,Yerror):
            print("\t\t\tX\tY\txerror\tyerror\t\\\\")
            for i,x in enumerate(X):
                if isinstance(x,Werttupel) and isinstance(Y[i],Werttupel):
                    print("\t\t\t" , x.Wert , "\t" , Y[i].Wert , "\t" , Xerror[i], "\t" , Yerror[i], "\t\\\\")
                elif isinstance(x,Werttupel):
                    print("\t\t\t" , x.Wert , "\t" , Y[i] , "\t" , Xerror[i] , "\t" , Yerror[i] , "\t\\\\")
                elif isinstance(Y[i],Werttupel):
                    print("\t\t\t" , x , "\t" , Y[i].Wert , "\t" , Xerror[i] , "\t" , Yerror[i] , "\t\\\\")
                else:
                    print("\t\t\t" , x , "\t" , Y[i] , "\t" , Xerror[i] , "\t" , Yerror[i] , "\t\\\\")
        if Conf[1] == 0:
            print("\\begin{figure}[H]\n")
        elif Conf[1] == 1:
            print("\\begin{subfigure}[b]{0.4\\textwidth}\n")
        else:
            print("Fehlerhafte Konfigurationsanweisung!")
            exit()
        print("\t\\centering\n\t\\begin{tikzpicture}\n\t\t\\pgfplotsset{width=6.5cm,compat=1.3,legend style={font=\\footnotesize}}\n\t\t\\begin{axis}[xlabel={" + Labels[0] + "},ylabel={" + Labels[1] + "},legend cell align=left,legend pos=north west]\n\t\t")      
        for i,(x,y) in enumerate(zip(X,Y)):
            print("\\addplot+[only marks,color=" + colors[i % len(colors)] + ",mark=square,error bars/.cd,x dir=both,x explicit,y dir=both,y explicit,error bar style={color=black}] table[x=X,y=Y,x error=xerror,y error=yerror,row sep=\\\\]{")
            Tabellenblock(x,y,Xerror,Yerror[i])
            print("\t\t};")
            print("\t\t% \\addlegendentry{Messpunkte Datensatz " + str(i) + "}\n")
            if RegSetting[i] == 1:
                print("\t\t\\addplot[] table[row sep=\\\\,y={create col/linear regression={y=Y}}]{")
                Tabellenblock(x,y,Xerror,Yerror[i])
                print("\t\t};")
                print("\t\t\\addlegendentry{%\n\t\t\t$\pgfmathprintnumber{\pgfplotstableregressiona} \cdot x\pgfmathprintnumber[print sign]{\pgfplotstableregressionb}$ lin. Regression} %")
            else:
                continue
        
        print("\t\t\\end{axis}\n\t\t\\end{tikzpicture}")
        print("\t\\caption{" + Caption + "}\n\t\\label{fig:" + Label + "}")
        
        if Conf[1] == 0:
            print("\\end{figure}")
        elif Conf[1] == 1:
            print("\\end{subfigure}")
        else:
            print("Fehlerhafte Konfigurationsanweisung!")
            exit()
    else:
        pass
    
def fileStandardPGFPlot(
        X: list,
        Y: list,
        Xerror: list,
        Yerror: list,
        RegSetting: list,
        Labels: list,
        Caption: str,
        Label: str,
        Conf: list,
        file
    ):
    colors = ["red","blue","green","yellow","orange","brown","pink"]
    
    if Conf[0] != 0:
        def Tabellenblock(X,Y,Xerror,Yerror):
            file.write("\t\t\tX\tY\txerror\tyerror\t\\\\")
            for i,x in enumerate(X):
                if isinstance(x,Werttupel) and isinstance(Y[i],Werttupel):
                    file.write("\t\t\t" + str(x.Wert) + "\t" + str(Y[i].Wert) + "\t" + str(Xerror[i]) + "\t" + str(Yerror[i]) + "\t\\\\")
                elif isinstance(x,Werttupel):
                    file.write("\t\t\t" + str(x.Wert) + "\t" + str(Y[i]) + "\t" + str(Xerror[i]) + "\t" + str(Yerror[i]) + "\t\\\\")
                elif isinstance(Y[i],Werttupel):
                    file.write("\t\t\t" + str(x) + "\t" + str(Y[i].Wert) + "\t" + str(Xerror[i]) + "\t" + str(Yerror[i]) + "\t\\\\")
                else:
                    file.write("\t\t\t" + str(x) + "\t" + str(Y[i]) + "\t" + str(Xerror[i]) + "\t" + str(Yerror[i]) + "\t\\\\")
        if Conf[1] == 0:
            file.write("\\begin{figure}[H]\n")
        elif Conf[1] == 1:
            file.write("\\begin{subfigure}[b]{0.4\\textwidth}\n")
        else:
            file.write("Fehlerhafte Konfigurationsanweisung!")
            exit()
        file.write("\t\\centering\n\t\\begin{tikzpicture}\n\t\t\\pgfplotsset{width=6.5cm,compat=1.3,legend style={font=\\footnotesize}}\n\t\t\\begin{axis}[xlabel={" + Labels[0] + "},ylabel={" + Labels[1] + "},legend cell align=left,legend pos=north west]\n\t\t")      
        for i,(x,y) in enumerate(zip(X,Y)):
            file.write("\\addplot+[only marks,color=" + colors[i % len(colors)] + ",mark=square,error bars/.cd,x dir=both,x explicit,y dir=both,y explicit,error bar style={color=black}] table[x=X,y=Y,x error=xerror,y error=yerror,row sep=\\\\]{")
            Tabellenblock(x,y,Xerror,Yerror[i])
            file.write("\t\t};")
            file.write("\t\t% \\addlegendentry{Messpunkte Datensatz " + str(i) + "}\n")
            if RegSetting[i] == 1:
                file.write("\t\t\\addplot[] table[row sep=\\\\,y={create col/linear regression={y=Y}}]{")
                Tabellenblock(x,y,Xerror,Yerror[i])
                file.write("\t\t};")
                file.write("\t\t\\addlegendentry{%\n\t\t\t$\pgfmathprintnumber{\pgfplotstableregressiona} \cdot x\pgfmathprintnumber[print sign]{\pgfplotstableregressionb}$ lin. Regression} %")
            else:
                continue
        
        file.write("\t\t\\end{axis}\n\t\t\\end{tikzpicture}")
        file.write("\t\\caption{" + Caption + "}\n\t\\label{fig:" + Label + "}")
        
        if Conf[1] == 0:
            file.write("\\end{figure}")
        elif Conf[1] == 1:
            file.write("\\end{subfigure}")
        else:
            file.write("Fehlerhafte Konfigurationsanweisung!")
            exit()
    else:
        pass
    
def LatexTabelle(Ueberschriften: list, Werte: list):
    tabularconfig = "c" * len(Werte[0])
    FormatUeberschrift = " & ".join(Ueberschriften)
    print("\\begin{table}[H]\m\t\\centering\n\t\\begin{tabular}" + tabularconfig + "\n\t\t" + FormatUeberschrift + "\\\\\n\t\t\\hline")
    for i in range(len(Werte[0])):
        print("\t\t" + " & ".join([s[i] for s in Werte]))
    print("\t\\end{tabular}\n\\end{table}")
    
def fileLatexTabelle(Ueberschriften: list, Werte: list, file):
    tabularconfig = "c" * len(Werte[0])
    FormatUeberschrift = " & ".join(Ueberschriften)
    file.write("\\begin{table}[H]\n\t\\centering\n\t\\begin{tabular}{" + tabularconfig + "}\n\t\t" + FormatUeberschrift + "\\\\\n\t\t\\hline\n")
    for i in range(len(Werte[0])):
        file.write("\t\t" + " & ".join(
            [str(s[i].Wert) if isinstance(s[i],Werttupel) else str(s[i]) for s in Werte]) + "\t\\\\\n"
        )
    file.write("\t\\end{tabular}\n\\end{table}")
            