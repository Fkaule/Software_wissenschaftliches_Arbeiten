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

class Plot_2(CodingProblem):
    _var = 'plt'
    _hint = ('keine Tipps hier')
    _solution = CS(
    """
    plt.plot(Temp_NASA2["Year"],Temp_NASA2["Land_Annual"], ls="-", lw=1, marker="s", ms=3, color="tab:red", alpha=0.5, label="Land");
    plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5)"], lw=3,  color="tab:red", label="Land (geglättet)");
    plt.plot(Temp_NASA2["Year"],Temp_NASA2["Ocean_Annual"], ls="-", lw=1, marker="s", ms=3, color="tab:blue", alpha=0.5, label="Ozean");
    plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5).1"], lw=3,  color="tab:blue", label="Ozean (geglättet)");
    plt.ylabel("Jahresmitteltemperaturabweichung [K]")
    plt.legend();
    plt.grid();
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Temp_NASA2["Year"],Temp_NASA2["Land_Annual"], ls="-", lw=1, marker="s", ms=3, color="tab:red", alpha=0.5, label="Land");
        plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5)"], lw=3,  color="tab:red", label="Land (geglättet)");
        plt.plot(Temp_NASA2["Year"],Temp_NASA2["Ocean_Annual"], ls="-", lw=1, marker="s", ms=3, color="tab:blue", alpha=0.5, label="Ozean");
        plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5).1"], lw=3,  color="tab:blue", label="Ozean (geglättet)");
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
        link = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/Temperature_Anomalies_over_Land_and_over_Ocean/graph.csv"
        Temp_NASA2 = pd.read_csv(link, header=1)
        # data 1
        x.append(Temp_NASA2["Year"]) 
        y.append(Temp_NASA2["Land_Annual"]) 
        # data 2
        x.append(Temp_NASA2["Year"]) 
        y.append(Temp_NASA2["Lowess(5)"]) 
        # data 3
        x.append(Temp_NASA2["Year"]) 
        y.append(Temp_NASA2["Ocean_Annual"]) 
        # data 4
        x.append(Temp_NASA2["Year"]) 
        y.append(Temp_NASA2["Lowess(5).1"]) 
        
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
        
        
class Plot_3(CodingProblem):
    _var = 'plt'
    _hint = ('keine Tipps hier')
    _solution = CS(
    """
    plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5)"], lw=3,  color="tab:red", label="global: Land (geglättet) [NASA]");
    plt.plot(Temp_GER["Jahr"],Temp_GER["Jahresmitteltemperaturabweichung [°C]"], ls="-", lw=1,marker="s", ms=3, color="gray",alpha=0.5, label="Deutschland Land (Jahreswerte) [DWD]");
    plt.plot(Temp_GER["Jahr"],Temp_GER["Lowess(own)"], ls="-", lw=2, color="black", label="Deutschland Land (geglättet) [DWD]");
    plt.ylabel("Jahresmitteltemperaturabweichung [K]")
    plt.legend(fontsize=12);
    plt.grid();
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Temp_NASA2["Year"],Temp_NASA2["Lowess(5)"], lw=3,  color="tab:red", label="global: Land (geglättet) [NASA]");
        plt.plot(Temp_GER["Jahr"],Temp_GER["Jahresmitteltemperaturabweichung [°C]"], ls="-", lw=1,marker="s", ms=3, color="gray",alpha=0.5, label="Deutschland Land (Jahreswerte) [DWD]");
        plt.plot(Temp_GER["Jahr"],Temp_GER["Lowess(own)"], ls="-", lw=2, color="black", label="Deutschland Land (geglättet) [DWD]");
        plt.ylabel("Jahresmitteltemperaturabweichung [K]")
        plt.legend(fontsize=12);
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
        link = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/Temperature_Anomalies_over_Land_and_over_Ocean/graph.csv"
        Temp_NASA2 = pd.read_csv(link, header=1)
        # data 1
        x.append(Temp_NASA2["Year"]) 
        y.append(Temp_NASA2["Lowess(5)"]) 
        
        link = "https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/3-bis-8_abb-tab_tmt_2021-05-12.xlsx"
        Temp_GER = pd.read_excel(link,sheet_name="3_DWD",usecols=[1,19]) # einlesen
        Temp_GER.columns=["Jahr","Jahresmitteltemperatur [°C]"]
        Temp_GER.dropna(inplace=True) # Zeilen mit "NaN" Werte rausschmeissen und dataframe speichern 
        Temp_GER["Jahr"] = Temp_GER["Jahr"].astype(int) # Spalte "Jahr" als integer definieren
        mean_GER1881_1910 = Temp_GER.loc[Temp_GER["Jahr"] <= 1910,"Jahresmitteltemperatur [°C]"].mean()
        Temp_GER["Jahresmitteltemperaturabweichung [K]"] = Temp_GER["Jahresmitteltemperatur [°C]"] - mean_GER1881_1910
        from statsmodels.nonparametric.smoothers_lowess import lowess
        Temp_GER["Lowess(own)"] = lowess(Temp_GER["Jahresmitteltemperaturabweichung [K]"],Temp_GER["Jahr"], frac=1/14)[:,1]
        
        # data 2
        x.append(Temp_GER["Jahr"]) 
        y.append(Temp_GER["Jahresmitteltemperaturabweichung [K]"]) 
        # data 3
        x.append(Temp_GER["Jahr"]) 
        y.append(Temp_GER["Lowess(own)"]) 
        
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
        
class Plot_4(CodingProblem):
    _var = 'plt'
    _hint = ('Für nur eine Linie ist kein `label` und damit auch keine Legende notwendig')
    _solution = CS(
    """
    plt.plot(THG_Emission_UBA["Jahr"],THG_Emission_UBA["CO2-eq\n(ppm)"], lw=3,  color="tab:red");
    plt.ylabel("CO2-Äquivalent [ppm]")
    plt.grid();
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(THG_Emission_UBA["Jahr"],THG_Emission_UBA["CO2-eq\n(ppm)"], lw=3,  color="tab:red");
        plt.ylabel("CO2-Äquivalent [ppm]")
        plt.grid();
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = ""
        y_label_einheit_truth = "ppm"
        
        # ground truth_data
        x = []
        y = []
        link = "https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/6_abb_treibhausgas-gesamt-konz_2020-06-03.xlsx"
        THG_Emission_UBA = pd.read_excel(link,sheet_name="Daten",usecols=[1,2],header=8) # einlesen
        # data 1
        x.append(THG_Emission_UBA["Jahr"]) 
        y.append(THG_Emission_UBA["CO2-eq\n(ppm)"]) 
        
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
        
        #assert legend_check == False, \
        #("Fügen Sie eine Legende mit `plt.legend()` hinzu")        
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("Ist der Plot eine Line-Chart? Bitte benutzen Sie `plt.plot()` um den plot zu erstellen ")

        assert anz_plots_check == anz_plots_truth, \
        ("Fehlerhafte Anzahl an Plots ") 

        assert data_right == True, \
        ("Die Daten stimmen nicht") 
        
        #assert len(legend_handles) == anz_plots_truth, \
        #("Sie haben `label=` nicht benutzt für die Legende")
        
class Plot_5(CodingProblem):
    _var = 'plt'
    _hint = ('Die Namen der Spalten finden Sie über `CO2_Emission_UBA.head()` ')
    _solution = CS(
    """
    plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Mauna Loa, Hawaii"], lw=2,  label="Mauna Loa, Hawaii", c="tab:orange");
    plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Schauinsland"], lw=2,  label="Schauinsland", c="tab:green");
    plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Zugspitze"], lw=2,  label="Zugspitze", c="tab:blue");
    plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Welttrend WMO"], lw=2,  label="Welttrend WMO", c="tab:red");
    plt.ylabel("$\mathrm{CO_2}$-Konzentration in der Atmosphäre [ppm]")
    plt.legend();
    plt.grid();
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Mauna Loa, Hawaii"], lw=2,  label="Mauna Loa, Hawaii", c="tab:orange");
        plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Schauinsland"], lw=2,  label="Schauinsland", c="tab:green");
        plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Zugspitze"], lw=2,  label="Zugspitze", c="tab:blue");
        plt.plot(CO2_Emission_UBA["Jahr"],CO2_Emission_UBA["Welttrend WMO"], lw=2,  label="Welttrend WMO", c="tab:red");
        plt.ylabel("$\mathrm{CO_2}$-Konzentration in der Atmosphäre [ppm]")
        plt.legend();
        plt.grid();
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = ""
        y_label_einheit_truth = "ppm"
        
        # ground truth_data
        x = []
        y = []
        link="https://www.umweltbundesamt.de/sites/default/files/medien/384/bilder/dateien/2-4_abb_langzeitreihen-konz_2021-05-26.xlsx"
        CO2_Emission_UBA = pd.read_excel(link,sheet_name="Kohlendioxid-Daten",usecols=[0,1,2,3,4]) # einlesen
        CO2_Emission_UBA.columns = ["Jahr","Mauna Loa, Hawaii","Schauinsland","Zugspitze","Welttrend WMO"]
        # data 1
        x.append(CO2_Emission_UBA["Jahr"]) 
        y.append(CO2_Emission_UBA["Mauna Loa, Hawaii"]) 
        # data 2
        x.append(CO2_Emission_UBA["Jahr"]) 
        y.append(CO2_Emission_UBA["Schauinsland"]) 
        # data 3
        x.append(CO2_Emission_UBA["Jahr"]) 
        y.append(CO2_Emission_UBA["Zugspitze"]) 
        # data 4
        x.append(CO2_Emission_UBA["Jahr"]) 
        y.append(CO2_Emission_UBA["Welttrend WMO"]) 
        
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
    Plot_2,
    Plot_3,
    Plot_4,
    Plot_5,
    ],
    start=1,
    )
__all__ = list(qvars)
