from learntools.core import *
from learntools.core.problem import injected

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

class Daten(EqualityCheckProblem):
    _vars = ["Weg","Kraft_Probe1","Kraft_Probe2"]
    _expected = [np.array([0,10,20,30,40]),
            np.array([10,18,24,28,30]),
            np.array([0,10,20,30,40]) 
            ]
    _hint = 'Verwenden Sie `np.array([])` und tragen Sie die Werte in den eckigen Klammern mit Komma getrennt ein'
    _solution = CS(
            "Weg = np.array([0,10,20,30,40])",
            "Kraft_Probe1 = np.array([10,18,24,28,30])",
            "Kraft_Probe2 = np.array([0,10,20,30,40])",
    )


    
    
class Plot_1(CodingProblem):
    _var = 'plt'
    _hint = "Nutzen Sie zwei mal plt.plot() jeweils mit `Weg` für `x` und `Kraft_Probe1` und `Kraft_Probe1` für `y` und unterscheiden Sie beide mit `label=` und fügen Sie die Legende mit `plt.legend()` hinzu"
    _solution = CS(
    """
    plt.plot(Weg,Kraft_Probe1,marker="s",label="Probe1");
    plt.plot(Weg,Kraft_Probe2,marker="s",label="Probe2");
    plt.legend()
    plt.xlabel("Weg [mm]");
    plt.ylabel("Kraft [N]");
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Weg,Kraft_Probe1,marker="s",label="Probe1");
        plt.plot(Weg,Kraft_Probe2,marker="s",label="Probe2");
        plt.legend();
        plt.xlabel("Weg [mm]");
        plt.ylabel("Kraft [N]");
  
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = "mm"
        y_label_einheit_truth = "N"
        
        # ground truth_data
        x = []
        y = []
        Weg = np.array([0,10,20,30,40])
        Kraft_Probe1 = np.array([10,18,24,28,30])
        Kraft_Probe2 = np.array([0,10,20,30,40])
        # data 1
        x.append(Weg) 
        y.append(Kraft_Probe1) 
        # data 2
        x.append(Weg) 
        y.append(Kraft_Probe2) 
        
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
        df_check = pd.concat(df_check_list, ignore_index=True)
        df_check = df_check.drop_duplicates().sort_values("x").reset_index(drop=True)
        
        # data check
        data_right = df_check.equals(df_truth)

        try:
            legend_check = main_axis.get_legend().get_title().get_visible()
        except:
            legend_check = True
               
        assert xlabel_check != "", \
        ("Fügen Sie eine Beschriftung der x-Achse hinzu")
        
        assert x_label_einheit_truth in xlabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der x-Achse hinzu")
        
        assert ylabel_check != "", \
        ("Fügen Sie eine Beschriftung der y-Achse hinzu")
        
        assert y_label_einheit_truth in ylabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der y-Achse hinzu")
        
        assert legend_check == False, \
        ("Fügen Sie eine Legende mit `plt.legend()` hinzu")        
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("Ist der Plot eine Line-Chart? Bitte benutzen Sie `plt.plot()` um den plot zu erstellen ")

        assert anz_plots_check == anz_plots_truth, \
        ("Es sollen 2 Verläufe erstellt werden. Es wurden aber %d erkannt ") % anz_plots

        assert data_right == True, \
        ("Die Daten stimmen nicht") 
        
        assert len(legend_handles) == anz_plots_truth, \
        ("Sie haben `label=` nicht benutzt für die Legende")

class Plot_2(CodingProblem):
    _var = 'plt'
    _hint = "Ziehen Sie für die y Koordinaten die Liste Kraft_Probe1 von der Liste Kraft_Probe2 ab "
    _solution = CS(
    """
    plt.plot(Weg,Kraft_Probe1-Kraft_Probe2,marker="s",label="Differenz Probe1-Probe2");
    plt.legend();
    plt.xlabel("Weg [mm]");
    plt.ylabel("Kraftdifferenz [N]");
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Weg,Kraft_Probe1-Kraft_Probe2,marker="s",label="Differenz Probe1-Probe2");
        plt.legend();
        plt.xlabel("Weg [mm]");
        plt.ylabel("Kraftdifferenz [N]");
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = "mm"
        y_label_einheit_truth = "N"
        
        # ground truth_data
        x = []
        y = []
        Weg = np.array([0,10,20,30,40])
        Kraft_Probe1 = np.array([10,18,24,28,30])
        Kraft_Probe2 = np.array([0,10,20,30,40])
        # data 1
        x.append(Weg) 
        y.append(Kraft_Probe1-Kraft_Probe2) 
        
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
        df_check = pd.concat(df_check_list, ignore_index=True)
        df_check = df_check.drop_duplicates().sort_values("x").reset_index(drop=True)
        
        # data check
        data_right = df_check.equals(df_truth)

        try:
            legend_check = main_axis.get_legend().get_title().get_visible()
        except:
            legend_check = True
               
        assert xlabel_check != "", \
        ("Fügen Sie eine Beschriftung der x-Achse hinzu")
        
        assert x_label_einheit_truth in xlabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der x-Achse hinzu")
        
        assert ylabel_check != "", \
        ("Fügen Sie eine Beschriftung der y-Achse hinzu")
        
        assert y_label_einheit_truth in ylabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der y-Achse hinzu")
        
        assert legend_check == False, \
        ("Fügen Sie eine Legende mit `plt.legend()` hinzu")        
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("Ist der Plot eine Line-Chart? Bitte benutzen Sie `plt.plot()` um den plot zu erstellen ")

        assert anz_plots_check == anz_plots_truth, \
        ("Es sollen 2 Verläufe erstellt werden. Es wurden aber %d erkannt ") % anz_plots

        assert data_right == True, \
        ("Die Daten stimmen nicht") 
        
        assert len(legend_handles) == anz_plots_truth, \
        ("Sie haben `label=` nicht benutzt für die Legende")
            
class Plot_3(CodingProblem):
    _var = 'plt'
    _hint = "Ziehen Sie für die y Koordinaten die Liste Kraft_Probe1 von der Liste Kraft_Probe2 ab "
    _solution = CS(
    """
    plt.plot(Weg,(Kraft_Probe1-Kraft_Probe2)/Kraft_Probe1*100,marker="s",label="Differenz Probe1-Probe2");
    plt.legend();
    plt.xlabel("Weg [mm]");
    plt.ylabel("Kraftdifferenz [%]");
    """)
    
    def solution_plot(self):
        self._view.solution()
        plt.plot(Weg,(Kraft_Probe1-Kraft_Probe2)/Kraft_Probe1*100,marker="s",label="Differenz Probe1-Probe2");
        plt.legend();
        plt.xlabel("Weg [mm]");
        plt.ylabel("Kraftdifferenz [%]");
    def check(self, passed_plt):
        
        assert len(passed_plt.figure(1).axes) > 0, \
        ("Fügen Sie den Code zum erstellen des plots hinzu. " 
         "Danach können Sie mit `check()` prüfen ob das Ergebnis korrekt ist")
        
        # ground truth
        x_label_einheit_truth = "mm"
        y_label_einheit_truth = "%"
        
        # ground truth_data
        x = []
        y = []
        Weg = np.array([0,10,20,30,40])
        Kraft_Probe1 = np.array([10,18,24,28,30])
        Kraft_Probe2 = np.array([0,10,20,30,40])
        # data 1
        x.append(Weg) 
        y.append((Kraft_Probe1-Kraft_Probe2)/Kraft_Probe1*100) 
        
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
        df_check = pd.concat(df_check_list, ignore_index=True)
        df_check = df_check.drop_duplicates().sort_values("x").reset_index(drop=True)
        
        # data check
        data_right = df_check.equals(df_truth)

        try:
            legend_check = main_axis.get_legend().get_title().get_visible()
        except:
            legend_check = True
               
        assert xlabel_check != "", \
        ("Fügen Sie eine Beschriftung der x-Achse hinzu")
        
        assert x_label_einheit_truth in xlabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der x-Achse hinzu")
        
        assert ylabel_check != "", \
        ("Fügen Sie eine Beschriftung der y-Achse hinzu")
        
        assert y_label_einheit_truth in ylabel_check, \
        ("Fügen Sie die Einheit in der Beschriftung der y-Achse hinzu")
        
        assert legend_check == False, \
        ("Fügen Sie eine Legende mit `plt.legend()` hinzu")        
        
        assert all(isinstance(x, matplotlib.lines.Line2D) for x in legend_handles), \
        ("Ist der Plot eine Line-Chart? Bitte benutzen Sie `plt.plot()` um den plot zu erstellen ")

        assert anz_plots_check == anz_plots_truth, \
        ("Es sollen 2 Verläufe erstellt werden. Es wurden aber %d erkannt ") % anz_plots

        assert data_right == True, \
        ("Die Daten stimmen nicht") 
        
        assert len(legend_handles) == anz_plots_truth, \
        ("Sie haben `label=` nicht benutzt für die Legende")
     

qvars = bind_exercises(globals(), [
    Daten,
    Plot_1,
    Plot_2,
    Plot_3,
    ],
    start=1,
    )
__all__ = list(qvars)
