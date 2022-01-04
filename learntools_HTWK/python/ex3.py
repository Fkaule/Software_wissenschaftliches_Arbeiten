# -*- coding: utf-8 -*-
from learntools.core import *
from learntools.core.problem import injected

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

class Plot_1(CodingProblem):
    _var = 'plt'
    _hint = ('<br>**Daten**: verwenden Sie `Temp_NASA["Year"]` als x-Variable und `Temp_NASA["No_Smoothing"]` sowie `Temp_NASA["Lowess(5)"]` als y-Variable und beschriften Sie beide mit label<br>' 
             '**Ploteinstellungen für die Jahreswerte** (Temp_NASA["No_Smoothing"]): Punkte: `marker="s"` (s=rechteckige Datenpunkte) / Punktgröße: `ms=3` (reduziert) / Liniendicke: `lw=1` (reduziert) / Farbe: `c="tab:blue"` (blau) mit Deckkraft: `alpha=0.5` (reduziert).<br>'
             '**Ploteinstellungen für die Glättung** (Temp_NASA["Lowess(5)"]) : Liniendicke: `lw=3` (verstärkt) / Farbe: `c="tab:blue"` (blau, gleiche wie bei den Datenpunkten)')
    _solution = CS(
    """
    plt.plot(Temp_NASA["Year"],Temp_NASA["No_Smoothing"], ls="-", lw=1, marker="s", ms=3, color="tab:blue", alpha=0.5, label="Werte");
    plt.plot(Temp_NASA["Year"],Temp_NASA["Lowess(5)"], lw=3,  color="tab:blue", label="geglättet");
    plt.ylabel("Jahresmitteltemperaturabweichung [K]")
    plt.legend();
    plt.grid();
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Temp_NASA["Year"],Temp_NASA["No_Smoothing"], ls="-", lw=1, marker="s", ms=3, color="tab:blue", alpha=0.5, label="Werte");
        plt.plot(Temp_NASA["Year"],Temp_NASA["Lowess(5)"], lw=3,  color="tab:blue", label="geglättet");
        plt.ylabel("Jahresmitteltemperaturabweichung [K]")
        plt.legend();
        plt.grid();
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = ""
        y_label_einheit_truth = "K"
        
        # ground truth_data
        x = []
        y = []
        link = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv"
        Temp_NASA = pd.read_csv(link, header=1) # einlesen
        # data 1
        x.append(Temp_NASA["Year"]) 
        y.append(Temp_NASA["No_Smoothing"]) 
        # data 2
        x.append(Temp_NASA["Year"]) 
        y.append(Temp_NASA["Lowess(5)"]) 
        
        anz_plots_truth = len(y) 

        # create df_truth
        df_truth_list = []
        for x,y in zip(x,y):
            data_tuples = list(zip(x,y))
            df = pd.DataFrame(data_tuples, columns=['x','y']).sort_values('x').reset_index(drop=True)
            df_truth_list.append(df)
        df_truth = pd.concat(df_truth_list, ignore_index=True)
        df_truth = df_truth.drop_duplicates().sort_values("x").reset_index(drop=True)
        df_truth

        # get check values from plot
        main_axis = passed_plt.figure(1).axes[0]
        legend_handles = main_axis.get_legend_handles_labels()[0]
        xlabel_check = main_axis.xaxis.get_label().get_text()
        ylabel_check = main_axis.yaxis.get_label().get_text()
        anz_plots_check = len(main_axis.get_lines())
        
        # create df_check 
        df_check_list = []
        for line in plt.gca().get_lines():
            x = line.get_xdata()
            y = line.get_ydata()
            data_tuples = list(zip(x,y))
            df_check = pd.DataFrame(data_tuples, columns=['x','y']).sort_values('x').reset_index(drop=True)
            df_check_list.append(df_check)   
        if len(df_check_list)>0: 
            df_check = pd.concat(df_check_list, ignore_index=True)
            df_check = df_check.drop_duplicates().sort_values("x").reset_index(drop=True)
        
            # data check
            data_right = df_check.equals(df_truth)

        try:
            legend_check = main_axis.get_legend().get_title().get_visible()
        except:
            legend_check = True
               
        #assert xlabel_check != "", \
        #("Fügen Sie eine Beschriftung der x-Achse hinzu")
        
        #assert x_label_einheit_truth in xlabel_check, \
        #("Fügen Sie die Einheit in der Beschriftung der x-Achse hinzu")
        
        assert ylabel_check != "", \
        ("Fügen Sie eine Beschriftung der y-Achse hinzu")
        
        assert y_label_einheit_truth in ylabel_check, \
        ("Fügen Sie die richtige Einheit in der Beschriftung der y-Achse hinzu (Temperaturdifferenzen in K)")
        
        assert legend_check == False, \
        ("Fügen Sie eine Legende mit `plt.legend()` hinzu")        
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("Ist der Plot eine Line-Chart? Bitte benutzen Sie `plt.plot()` um den plot zu erstellen ")

        assert anz_plots_check == anz_plots_truth, \
        ("Fehlerhafte Anzahl an Plots ") 

        assert data_right == True, \
        ("Die Daten stimmen nicht") 
        
        assert len(legend_handles) == anz_plots_truth, \
        ("Sie haben `label=` nicht benutzt für die Legende")


qvars = bind_exercises(globals(), [
    Plot_1,
    ],
    start=1,
    )
__all__ = list(qvars)
