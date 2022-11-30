# Mathematische Umgebungen

Mathematische Formeln können innerhalb des Textes oder als seperate Gleichung verwendet werden. Der verwendete Syntax ist bei beiden Fällen der gleiche. Zur Verwendung innerhalb des Textes wird dieser zwischen zwei Dollarzeichen eingebettet. Für eine Gleichung wird die `equation`-Umgebung verwendet, dort sind die Dollarzeichen nicht notwendig. Hier ein einfaches Beispiel mit beiden Anwendungen:

Hier ein erstes Beispiel:

```latex
\documentclass{scrreprt}
\begin{document}

Der Anstieg $m$ ergibt sich auf den Differenzen von $x$ und $y$ zu:
\begin{equation}
    m=\frac{\Delta y}{\Delta x}=\frac{y_1 - y_0}{x_1 - x_0}
\end{equation}

\end{document}
```

```{image} Einfuehrung/math1.png 
--- 
width: 700px 
align: center

``` 
<br><br>
Zur Erklärung:
- Mit dem Befehl `\frac{Zähler}{Nenner}` können Brüche dargestellt werden. 
- Mit `\Delta` wird der griechische Buchstabe Delta dargestellt. 
- Mit `_` wird ein Text tiefgestellt (wenn mehrere Zeichen mit Leerzeichen tiefgestellt werden soll müssen diese in geschweiften Klammern gesetzt werden, z.B. `x_{0,init}`)

Die Gleichung innerhalb der `equation`-Umgebung wird automatisch nummeriert. Da in diesem Fall kein Kapitel erstellt wird steht eine 0 in der Nummerierung. Mit einem Kapitel sieht es dann wie folgt aus:


```latex
\documentclass{scrreprt}
\begin{document}

\chapter{Einleitung}

Der Anstieg $m$ ergibt sich auf den Differenzen von $x$ und $y$ zu:
\begin{equation}
    m=\frac{\Delta y}{\Delta x}=\frac{y_1 - y_0}{x_1 - x_0}
\end{equation}

\end{document}
```

```{image} Einfuehrung/math2.png 
--- 
width: 700px 
align: center

``` 

## Zusammenfassung innerhalb der mathematischen Umgebung

- griechische Buchstaben z.B. `\alpha` oder pi mit `\pi`
- Quadratwurzel `\sqrt{}` .. kubische Wurzel `\sqrt[3]{}`
- `\sin()` ,  `\cos()` ...
- Brüche mit `\frac{}{}`
- hochstellen mit `^` bzw. `_{}`
- tiefstellen mit `_` bzw. `_{}`
- `\left(` und `\right(` große runde Klammern
- `\left[` und `\right[` große eckige Klammern

Weiterführendes Material dazu findet man in der [Overleaf Dokumentation](https://www.overleaf.com/learn/latex/Mathematical_expressions)^x

## Gleitkommawerte und Einheiten

Bei Gleitkommawerte und Einheiten werden standardmäßig von LaTeX nicht richtig dargestellt: 
1. Bei Gleitkommawerten wird durch das `,` ein Leerzeichen eingefügt, weil LaTeX davon ausgeht, dass es sich um eine Auflistung handelt. 
2. Einheiten werden ebenfalls kursiv dargestellt und ohne Leerzeichen. Dies entspricht jedoch nicht den gängigen Vorgaben. 

Am nachfolgenden Beispiel kann man die falsche Darstellung (Standardvariante) und eine richtige Darstellung sehen:

````{tabbed} falsche Darstellung (Standardausgabe)
```{image} Einfuehrung/unit1.png 
``` 
````

````{tabbed} richtige Darstellung
```{image} Einfuehrung/unit2.png 
``` 
````

Nachfolgend der Code für die Standardvariante und zwei Versionen mit der richtigen Darstellung:


````{tabbed} falsche Darstellung (Standardausgabe)
```latex
\documentclass{scrreprt}
\begin{document}
$37,58 km/h$
\end{document}
```
```{image} Einfuehrung/unit_wrong.png 
--- 
width: 100px 
align: center

``` 
````

````{tabbed} richtige Darstellung (händisch)
```latex
\documentclass{scrreprt}
\begin{document}
$37{,}58\,\mathrm{km/h}$
\end{document}
```
```{image} Einfuehrung/unit_right.png 
--- 
width: 100px 
align: center

``` 

- Komma in geschweiften Klammern `{,}`
- halber Zeilenabstand nach Zahl mit `\,`
- kursive Schrift entfernen für Einheiten mit `\mathrm{}`
````

````{tabbed}  richtige Darstellung (siunitx-Paket)
```latex
\documentclass{scrreprt}
\usepackage{siunitx}
\sisetup{locale = DE}
\begin{document}
$\SI{37,58}{km/h}$
\end{document}
```
```{image} Einfuehrung/unit_right.png 
--- 
width: 100px 
align: center

``` 

- Verwendung von `siunitx` - Paket und Einstellung auf deutsch mit `\sisetup{locale = DE}`
- Syntax: $\SI{Zahl}{Einheit}
- [Ausführlichen Erklärung zu dem Paket von Tobias Weh](https://tobiw.de/tbdm/siunitx)
````

## Wertebereiche

Mit `\SIrange{}{}` können Wertebereiche dargestellt werden. Damit diese im Deutschen mit dem Wort `bis` richtig dargestellt werden, muss der Parameter `ngerman` in der Klassendefinition übergeben werden:

````{tabbed} falsche Darstellung (ngerman in Paket babel)
```latex
\documentclass{scrreprt}

\usepackage[ngerman]{babel}
\usepackage{siunitx}
\sisetup{locale=DE}

\begin{document}

Eine Kraft von \SIrange{100}{400}{\newton}

\end{document}
```
```{image} Einfuehrung/siunitx_range_wrong.png 
--- 
width: 300px 
align: center

``` 
---
- `ngerman` im `Paket` (`babel`) übergeben führt nicht zum gewollten Ergebnis
````

````{tabbed} richtige Darstellung (ngerman in Klasse)
```latex
\documentclass[ngerman]{scrreprt}

\usepackage{babel}
\usepackage{siunitx}
\sisetup{locale=DE}

\begin{document}

Eine Kraft von \SIrange{100}{400}{\newton}

\end{document}
```
```{image} Einfuehrung/siunitx_range_right.png 
--- 
width: 300px 
align: center

``` 
---
- `ngerman` in der `Klasse` übergeben führt zum gewollten Ergebnis
````


## Einheiten in Tabellen
<a id='Tabelle_mit_Einheiten'></a>

[Auf der Seite von Tobias Weh](https://tobiw.de/tbdm/siunitx) zur dem Einheitenpaket `siunitx` gibt es noch ein schönes Beispiel für eine Tabelle mit Einheiten. Dabei werden die Zahlen automatisch gerundet und entsprechend dem Dezimantrenner ausgerichtet. 

````{tabbed} Darstellung
```{image} Einfuehrung/unit_tab.png 
--- 
width: 400px 
align: center

``` 
````

````{tabbed} Code
```latex
\documentclass{scrreprt}

\usepackage{booktabs}
\usepackage{siunitx}

\sisetup{
   locale = DE,
   per-mode = fraction,% | reciprocal | fraction | …
%   separate-uncertainty,
%   exponent-to-prefix,
   prefixes-as-symbols = false,
   list-units = brackets,% | single | repeat
   range-units = brackets,% | single | repeat
   multi-part-units = brackets,% | single | repeat
   table-unit-alignment = left,
}

\begin{document}

\begin{table}[hb]
   \centering
   \caption{Naturkonstanten}
   \begin{tabular}{
      l
      S[round-mode=places, round-precision=2]
      s[per-mode=symbol]
   }
      \toprule
         {Name} & {Wert} & {Einheit} \\
      \midrule
         Lichtgeschwindigkeit $c$ & 2,99792458e8 & m/s \\
         Gravitationskonstante $\gamma$ & 6,67428e-11 &
            \N\m\squared\per\kg\squared \\
         Elementarladung $e$ & 1,602176487e-19 & \coulomb \\
      \bottomrule
   \end{tabular}
\end{table}

\end{document}
``` 
````





