# Tabellen

Zugegeben, Tabellen sind nicht so einfach zu erstellen in LaTeX. Es ist weniger die Schwierigkeit, als mehr der Aufwand, den sie beim erstellen erzeugen.

## Tabellenlayout

Wir starten mit einer einfachen 2 x 4 Tabelle. Dazu verwenden wir als äußere Klammer die `table`-Umgebung. Innerhalb dieser kann mit `\centering` die Tabelle zentriert werden. Der Inhalt der Tabelle wird im Inneren der `table`-Umgebung mittels der `tabular`-Umgebung definiert.

Bei der Definition der `tabular`-Umgebung werden die Spalten und die Ausrichtung erstellt:

- `l` - links
- `r` - rechts
- `c` - mittig

Für den ersten Fall mit zwei mittig zentrieren Spalten sieht es dann so aus: `\begin{tabular}{ c c }`

Die gesamte Tabelle würde dann so aussehen:

::::{grid}
:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \begin{tabular}{ c c }
   Zelle1 & Zelle2  \\
   Zelle3 & Zelle4  \\
   Zelle5 & Zelle6  \\
   Zelle7 & Zelle8
 \end{tabular}
\end{table}
```

:::
:::{grid-item-card} Output

```{image} Einfuehrung/tab1.png
:width: 150px
:align: center
```

:::
::::

Für eine 3x3 Tabelle sieht es dann so aus:

::::{grid}

:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \begin{tabular}{ c c c }
   Zelle1 & Zelle2 & Zelle3 \\
   Zelle4 & Zelle5 & Zelle6 \\
   Zelle7 & Zelle8 & Zelle9
 \end{tabular}
\end{table}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/tab2.png
:width: 250px
:align: center
```

:::

::::

Mit `|` zwischen den Spaltenausrichtungen können vertikale Linien eingefügt werden:

::::{grid}

:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \begin{tabular}{|c|c|c|}
   Zelle1 & Zelle2 & Zelle3 \\
   Zelle4 & Zelle5 & Zelle6 \\
   Zelle7 & Zelle8 & Zelle9
 \end{tabular}
\end{table}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/tab3.png
:width: 280px
:align: center
```

::::

Mit `\hline` können horizontale Linien eingefügt werden:

::::{grid}

:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \begin{tabular}{|c|c|c|}
   \hline
   Zelle1 & Zelle2 & Zelle3 \\
   \hline
   Zelle4 & Zelle5 & Zelle6 \\
   \hline
   Zelle7 & Zelle8 & Zelle9 \\
   \hline
 \end{tabular}
\end{table}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/tab4.png
:width: 280px
:align: center
```

::::

Um ein Tabellenheader einzufügen könnte man z.B. die Schrift mit `\textbf{}` **fett** drucken um diese hervorzuheben:

::::{grid}

:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \begin{tabular}{|c|c|c|}
   \hline
   \textbf{Header1} &
   \textbf{Header2} &
   \textbf{Header3} \\
   \hline
   Zelle1 & Zelle2 & Zelle3 \\
   \hline
   Zelle4 & Zelle5 & Zelle6 \\
   \hline
   Zelle7 & Zelle8 & Zelle9 \\
   \hline
 \end{tabular}
\end{table}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/tab5.png
:width: 280px
:align: center
```

::::

## Tabellenüberschrift & Verweise

Analog wie bei Abbildungen können mit `\label{name}` und `\ref{name}` auf Tabellennummern verwiesen werden. Mit `\caption{Tabellenüberschrift}` kann die Tabellenüberschrift erstellt werden.

::::{grid}

:::{grid-item-card} Input

```latex
\begin{table}
 \centering
 \caption{Meine erste eigene Tabelle}
 \label{tab:erste_Tabelle}
 \begin{tabular}{|c|c|c|}
  \hline
  \textbf{Header1} &
  \textbf{Header2} &
  \textbf{Header3} \\
  \hline
  Zelle1 & Zelle2 & Zelle3 \\
  \hline
  Zelle4 & Zelle5 & Zelle6 \\
  \hline
  Zelle7 & Zelle8 & Zelle9 \\
  \hline
 \end{tabular}
\end{table}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/tab5b.png
:width: 250px
:align: center
```

::::

## Tabellenposition

Analog zu Abbildungen kann man LaTeX mit der Positionsangabe `[!h]` anschließend an `\begin{table}` die Positionswünsche übermitteln. Möglich sind:

    - `h` - here - bitte versuche es genau an dieser Textstelle
    - `t` - top - wenn möglich an Oberkante der Seite
    - `b` - bottom - wenn möglich, an Unterkante der Seite
    - `p` - page - nutze eine extra Seite für die Bilder
    - Mit dem `!` erhöht man die Priorität seiner Forderung, man "zwingt" LaTeX zur Umsetzung.

## komplexere Tabelle mit zusätzlichen Paketen

Um komplexere Tabellen zu erzeugen sind zusätzliche Pakete wie `booktabs` , `multirow` und `makecell` notwendig. Nachfolgend wir dies an einem Beispiel dargestellt:

::::{tab-set}

:::{tab-item} Beispiel 1

```{image} Einfuehrung/nice_tables1.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\begin{document}

\begin{table}
 \begin{tabular}{lcccc}
 \hline
 Name    & Header1  & Header2  & Header3  & Header4  \\
 \hline
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \hline
 \end{tabular}
\end{table}

\end{document}
```

- Ausgangsbeispiel ohne weitere Pakete
  :::

:::{tab-item} Beispiel 2

```{image} Einfuehrung/nice_tables2.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 Name    & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- Verwendung des Pakets `booktabs` für `\toprule` , `\midrule` und `\bottomrule` (verbesserte horizontale Linien)
- `@{}` am Anfang und `@{}` am Ende in `\begin{tabular}{}` verkürzt die Tabelle links und rechts auf das nötigste

:::

:::{tab-item} Beispiel 3

```{image} Einfuehrung/nice_tables3.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 \multicolumn{1}{c}{Name} & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- `\multicolumn{1}{c}{Name}` um die Überschrift `Name` zu zentrieren obwohl die Spalte eigentlich linksausgerichtet ist

:::

:::{tab-item} Beispiel 4

```{image} Einfuehrung/nice_tables4.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 \multicolumn{1}{c}{Name}    & \multicolumn{2}{c}{Overhead1}  & \multicolumn{2}{c}{Overhead2}  \\
                             & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- `\multicolumn{2}{c}{Text}` fasst zwei Spalten zusammen (in dem Beispiel für die Überschrift)

:::

:::{tab-item} Beispiel 5

```{image} Einfuehrung/nice_tables5.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs, multirow}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 \hfil\multirow{2}{*}{Name}    & \multicolumn{2}{c}{Overhead1}  & \multicolumn{2}{c}{Overhead2}  \\
                             & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- `\multirow{2}{*}{Name}` zentriert Name vertikal in dem es zwei Zeilen zusammenfuegt (durch Paket `multirow`)
- `\hfil` vor `\multirow` sorgt dafür das Name horizontal wieder zentriert wird

:::

:::{tab-item} Beispiel 6

```{image} Einfuehrung/nice_tables6.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs, multirow}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 \hfil\multirow{2}{*}{\textbf{Name}}    & \multicolumn{2}{c}{\textbf{Overhead1}}  & \multicolumn{2}{c}{\textbf{Overhead2}}  \\
                             & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & text text text & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- mit `\textbf{}` kann die Überschrift zusätzlich hervorgehoben werden

:::

:::{tab-item} Beispiel 7

```{image} Einfuehrung/nice_tables7.png
---
width: 400px
align: center

```

```latex
\documentclass{scrreprt}
\usepackage{booktabs, multirow, makecell}
\begin{document}

\begin{table}
\begin{tabular}{@{} lcccc @{}}
 \toprule
 \hfil\multirow{2}{*}{\textbf{Name}}    & \multicolumn{2}{c}{\textbf{Overhead1}}  & \multicolumn{2}{c}{\textbf{Overhead2}}  \\
                             & Header1  & Header2  & Header3  & Header4  \\
 \midrule
 Name A & \makecell[c]{text oben \\ text unten} & text text & text text & text text \\
 Name B & text text & text text & text text text & text text \\
 \bottomrule
 \end{tabular}
\end{table}

\end{document}
```

- mit `\makecell[c]{text oben \\ text unten}` wurde ein Textumbruch innerhalb einer Zelle erzeugt (c=zentriert) (Paket `makecell`)

:::

::::

## zu breite Tabellen

Wenn Tabellen zu breit werden gibt es verschiede Möglichkeiten das Problem zu lösen:

1. Zeilenbreite festlegen mit `p{breite}` statt `c` , `l` oder `r` in der Defintion der Tabelle, wie hier z.B.: `\begin{tabular}{c|c|p{4cm}}` erstellt zwei Spalten zentriert (ohne Größenangabe) und eine Spalte mit 4cm Breite
2. Manuellen Zeilumbruch mit dem Paket `makecell` z.B. so: `\makecell[c]{text oben \\ text unten}`
3. vertikale Linien zwischen Spalten entfernen mit `\tabcolsep=0.11cm` vor tabular Umgebung
4. Gesamte Schriftgröße skalieren durch folgende Befehle innerhalb vor tabular Umgebung: `\small` oder `\footnotesize`

## Einheiten und Zahlenwerte in Tabellen

In dem Abschnitt zur Verwendung von Einheiten gibt es Beispiel zur Verwendung von Einheiten und Zahlen in Tabellen mit dem Paket `unitx`. Dabei werden die Zahlen automatisch gerundet und entsprechend dem Dezimantrenner ausgerichtet ([Link](Einfuehrung.html#Tabelle_mit_Einheiten)).
