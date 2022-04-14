# Einführung

## Links

[Overleaf Dokumentation (englisch)](https://www.overleaf.com/learn/latex/Main_Page)

## Editor

Es gibt für LaTeX mittlerweile zwei prinzipielle Möglichkeiten:

- online im Webbrowser
    - [Overleaf](https://www.overleaf.com/)

- Installation auf dem eigenen Rechner
    - Windows [MiKTeX](https://miktex.org/)
    - Windows [Tex Live](https://www.tug.org/texlive/)
    - Mac [MacTeX - TeX Users Group](https://tug.org/mactex/)
    - Linux [ubuntuusers.de](https://wiki.ubuntuusers.de/TeX_Live/)

Für uns ist im Moment die Nutzung online am einfachsten und sehr direkt umsetzbar. Daher bitte bei Overleaf einen Account (kostenlos) anlegen. Dann kann es losgehen ...

## Ein erstes "Hallo Welt"

Nachfolgend erste und einfachste LaTeX Dokument. Es muss immer eine **Dokumenteklasse** definiert werden und der eigentliche Inhalt (in diesem Fall nur ein einfacher Text) steht immer innerhalb von `\begin{document}` und `\end{document}`

````{panels}
Input
^^^
```latex
\documentclass{article}
\begin{document}
    Hallo Welt.
\end{document}
```
---
Output
^^^
```{image} Einfuehrung/Untitled.png 
``` 
````


# Präambel des Dokuments

Die Präambel beschreibt alles was vor `\begin{document}` steht. Dabei geht es um die **Grundeinstellungen** des Dokumentes. Konkret wird folgendes definiert:

1. Dokumentenklasse (Layout der Seite)
2. Pakete (ermöglichen zusätzliche Funktionen)

## Dokumentklassen

Mit der Definition der Dokumentenklasse beginnt das LaTeX Dokument. Mit der Dokumentenklasse wird das **Layout** des Dokuments bestimmt.

```latex
\documentclass{name}
\begin{document}
    ....
\end{document}
```

- name=`article` - für kleinere Texte, beinhaltet keine Kapitelüberschriften
- name=`report` - Berichte, Abschlussarbeiten, beinhaltet Kapitelüberschriften
- name=`book` - umfangreiche Texte, beinhaltet Kapitelüberschriften und ist standardmäßig zweiseitig

Es gibt ähnliche Klassen, die zum modernen und weitverbreiteten KOMA-Skript gehören. Diese lauten dann:

- name=`scrartcl`
- name=`scrreprt`
- name=`scrbook`

Wir werden im weiteren Verlauf vor allem auf `scrreprt` setzen, da diese Klasse nahe einer Abschlussarbeit kommt und damit gut zu uns passt.

Es gibt noch weitere Klassen zum Schreiben von Briefen (dinbrief) o.ä., die wir hier aber nicht genauer betrachten wollen. Ist der Einstieg in LaTeX geschafft, kann man diese auch schnell selbst einbinden.


## sinnvolle Pakete (packages)

In der Präambel nach der Dokumentenklasse können Pakete (packages) verwendet werden die bestimmte Funktionen hinzufügen. Dies kann z.B. eine automatische Silbentrennung sein. Diese Pakete werden mit dem Befehl `\usepackage[option]{name}` eingefügt: 

```latex
\documentclass{scrreprt}

\usepackage[option]{name} 

\begin{document}
    ....
\end{document}
```

Besonders sinnvolle packages sind hier zusammengefasst:

```latex
\usepackage[ngerman]{babel} % deutsche Spracheinstellung
\usepackage[utf8]{inputenc} % Zeichenkodierung für UTF-8 (Unicode) falls Editor es unterstützt (bevorzugt)
% \usepackage[latin1]{inputenc} % Zeichenkodierung unter Windows für Umlaute und Sonderzeichen falls kein UTF-8 im Editor
\usepackage[T1]{fontenc} % Korrektes Trennen von Wörtern mit Umlauten und Akzenten.
\usepackage{graphicx} % Grafiken einbinden
```

# Gliederung und Verzeichnisse

## Überschriftsebenen

Es gibt maximal drei nummerierte Ebenen für die Dokumentstruktur:

**article-Klassen** `\documentclass{article}`:

````{panels}
Input
^^^
```latex
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```
---
Output
^^^
```{image} Einfuehrung/Untitled_1.png 
``` 
````

**report/book-Klassen** `\documentclass{report}` oder `\documentclass{book}`:

````{panels}
Input
^^^
```latex
\chapter{Kapitelüberschrift}
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```
---
Output
^^^
```{image} Einfuehrung/Untitled_2.png 
``` 
````

## Inhaltsverzeichnis


````{panels}
Input
^^^
```latex
\tableofcontents % Inhaltsverzeichnis
\listoffigures % Abbildungsverzeichnis
```
---
Output
^^^
```{image} Einfuehrung/Untitled_3.png 
``` 
```{image} Einfuehrung/Untitled_4.png 
``` 
````


# Abbildungen

Das Einfügen von Bildern ist in LaTeX besonders einfach und ungewohnt (wenn man Word gewohnt ist) zugleich. 

**EINFACH** - da LaTeX die Aufgabe übernimmt, das Bild vernünftig zum Text zu positionieren. 

**UNGEWOHNT** - da LaTEX die Aufgabe übernimmt, das Bild vernünftig zum Text zu positionieren. Daher der Rat: Erzwingen Sie nichts, sondern vertrauen Sie LaTeX.

Generell gilt für eine gute Bildposition im wissenschaftlichen Text:

- Bilder werden nicht vom Text umflossen, sondern nehmen als Objekt die gesamte Textbreite ein
- Bilder sollten am unteren oder oberen Rand der Seite positioniert werden, um den Textfluss nicht zu stören.
- Bilder sollten, wenn möglich, die Textbreite nutzen. Eventuell auch mehrere Bilder in einer Abbildungsumgebung unterbringen, wenn es inhaltlich sinnvoll ist.

## Paket `graphicx`

Um Bilder einzufügen muss das Paket `graphicx` verwendet werden. Dafür in die Präambel (vor `\begin{document}`) der Text `\usepackage{graphicx}` einfügt werden:

```latex
\documentclass{scrreprt}

\usepackage{graphicx} 

\begin{document}
    ....
\end{document}
```

## Abbildung einfügen

Innerhalb der `document`-Umgebung (nach `\begin{document}`) können Bilder eingefügt werden. Dafür wird eine `figure`-Umgebung erstellt (mit `\begin{figure}` und `\end{figure}`). Innerhalb dieser Umgebung kann dann mit \includegraphics{bild.png} z.B. eine Datei `bild.png` eingefügt  werden. Konkret wird dies am nachfolgenden Beispiel verdeutlicht:


```latex
\begin{document}
%...
... Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat (s. Abb. \ref{fig:bildlabel}). 
%
\begin{figure}[!h] %Postionsangabe
    \centering
    \includegraphics[width=60mm]{dependency.png}
    \caption{Ein Bild zur Digitalisierung. Quelle: xkcd.com}
    \label{fig:bildlabel}
\end{figure}
%
Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
%...
\end{document}
```

```{image} Einfuehrung/Untitled_5.png 
--- 
width: 500px 
align: center
``` 

<br>
Nachfolgend nun die Erklärungen zu den Befehlen:

## Referenzierungen

- `\label{label_name}` (innerhalb von der `figure`-Umgebung) erstellt ein label welches im Text (also außerhalb der `figure`-Umgebung) mit dem Befehl `\ref{label_name}` referenziert werden kann.  Es wird dann die zugehörige Nummer eingefügt.
- `\includegraphics[width=60mm]{dependency.png}` wird die Bilddatei `dependency.png` mit einer Breite von 60mm eingefügt. Die Datei liegt dabei im gleichen Verzeichnis wie die LaTeX Datei, es sind aber auch relative Pfade möglich (z.B. in einen Ordner Abbildungen  `\includegraphics{Abbildungen/dependency.png}`). Es können Bilder mit der Dateieindung `.png` , `.jpg` und `.jpeg` standardmäßig verwendet werden.

## Bildposition 

Mit der Positionsangabe `[!h]` kann man LaTeX Hinweise zu den Positionswünschen übermitteln. Möglich sind:

- `h` - here - bitte versuche es genau an dieser Textstelle
- `t` - top - wenn möglich an Oberkante der Seite
- `b` - bottom - wenn möglich, an Unterkante der Seite
- `p` - page - nutze eine extra Seite für die Bilder
- Mit dem `!` erhöht man die Priorität seiner Forderung, man "zwingt" LaTeX zur Umsetzung.
    

## Bildgröße 

Die Bildgröße kann wie folgt beschrieben werden:

- `\includegraphics{bild.png}` : Originalbreite des Bildes wird verwendet
- `\includegraphics[width=60mm]{bild.png}` : Die Breite wird auf 60mm festgelegt
- `\includegraphics[width=0.25\textwidth]{bild.png}` : Die Breite wird auf 25% der Seitenbreite festgelegt

## Bilderunterschriften 

Mit `\caption{...}` wird die Bildunterschrift definiert. Um die Bildunterschrift optisch ansprechender zu gestalten wird kann das Paket `caption` verwendet werden mit den Optionen `labelfont=bf,font=small,textfont=it` 

```latex
...
\usepackage{caption}
\captionsetup{labelfont=bf,font=small,textfont=it}
...
\begin{document}
...
```

Hier der Unterschied zwischen der Standardvariante und der verbesserten Variante:

````{tabbed} Bildunterschrift Standard
```{image} Einfuehrung/Untitled_6.png 
``` 
````

````{tabbed} Bildunterschrift verbessert (mit caption-Paket)
```{image} Einfuehrung/Untitled_7.png 
``` 
````

## Mehrere Abbildungen in einer Figure Umgebung (subfigure)

Es gibt verschiedene Variante wie man mehrere Bilder in einer `figure`-Umgebung platzieren kann. Hier ein Beispiel in dem das Paket `subcaption` benutzt wird und die Bilder in einer `\subcaptionbox` erstellt werden:

````{tabbed} ohne /hfill
```{image} Einfuehrung/subfig1.png 
--- 
width: 500px 
align: center

``` 
```latex
\usepackage{graphicx} % Grafiken
\usepackage{subcaption} % subfigures

\begin{document}

\begin{figure}[h!]
\centering
\label{fig:HTWK_Logos}
\subcaptionbox{HTWK}{\includegraphics[width=.45\linewidth]{HTWK.png}}
\subcaptionbox{ING}{\includegraphics[width=.45\linewidth]{ING.png}}
\caption{HTWK Logos ohne hfill}
\end{figure}

\end{document}
```
- Bilder werden standardmäßig nebeinander ohne Abstand dargestellt (so nicht gewünscht)
````

````{tabbed} mit /hfill
```{image} Einfuehrung/subfig2.png 
--- 
width: 500px 
align: center

``` 
```latex
\usepackage{graphicx} % Grafiken
\usepackage{subcaption} % subfigures

\begin{document}

\begin{figure}[h!]
\centering
\label{fig:HTWK_Logos}
\subcaptionbox{HTWK}{\includegraphics[width=.45\linewidth]{HTWK.png}}\hfill
\subcaptionbox{ING}{\includegraphics[width=.45\linewidth]{ING.png}}
\caption{HTWK Logos ohne hfill}
\end{figure}

\end{document}
```
- wird nach der `\subcaptionbox` ein `\hfill` verwendet, verteilt sich der Inhalt auf der Seitenbreite
````

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

````{panels}
Input
^^^
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
---
Output
^^^
```{image} Einfuehrung/tab1.png 
:width: 200px
:align: center
``` 
````

Für eine 3x3 Tabelle sieht es dann so aus:


````{panels}
Input
^^^
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
---
Output
^^^
```{image} Einfuehrung/tab2.png 
:width: 300px
:align: center
``` 
````

Mit `|` zwischen den Spaltenausrichtungen können vertikale Linien eingefügt werden:


````{panels}
Input
^^^
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
---
Output
^^^
```{image} Einfuehrung/tab3.png 
:width: 300px
:align: center
``` 
````

Mit `\hline` können horizontale Linien eingefügt werden:


````{panels}
Input
^^^
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
---
Output
^^^
```{image} Einfuehrung/tab4.png 
:width: 300px
:align: center
``` 
````

Um ein Tabellenheader einzufügen könnte man z.B. die Schrift mit `\textbf{}` **fett** drucken um diese hervorzuheben:


````{panels}
Input
^^^
```latex
\begin{table}
 \centering
 \begin{tabular}{|c|c|c|}
   \hline
   \textbf{Header1} & \textbf{Header2} & \textbf{Header3} \\
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
---
Output
^^^
```{image} Einfuehrung/tab5.png 
:width: 300px
:align: center
``` 
````

## Tabellenüberschrift & Verweise

Analog wie bei Abbildungen können mit `\label{name}` und  `\ref{name}` auf Tabellennummern verwiesen werden. Mit `\caption{Tabellenüberschrift}` kann die Tabellenüberschrift erstellt werden.


````{panels}
Input
^^^
```latex
\begin{table}
 \centering
 \caption{Meine erste eigene Tabelle}
 \label{tab:erste_Tabelle}
 \begin{tabular}{|c|c|c|}
  \hline
  \textbf{Header1} & \textbf{Header2} & \textbf{Header3} \\
  \hline
  Zelle1 & Zelle2 & Zelle3 \\
  \hline
  Zelle4 & Zelle5 & Zelle6 \\  
  \hline
  Zelle7 & Zelle8 & Zelle9 \\ 
  \hline
 \end{tabular}
\end{table}
%
... sind die Werte in Tabelle \ref{tab:erste_Tabelle} zusammengefasst.

```
---
Output
^^^
```{image} Einfuehrung/tab5b.png 
``` 
````

## Tabellenposition 

Analog zu Abbildungen kann man LaTeX mit der Positionsangabe `[!h]` anschließend an `\begin{table}` die Positionswünsche übermitteln. Möglich sind:

    - `h` - here - bitte versuche es genau an dieser Textstelle
    - `t` - top - wenn möglich an Oberkante der Seite
    - `b` - bottom - wenn möglich, an Unterkante der Seite
    - `p` - page - nutze eine extra Seite für die Bilder
    - Mit dem `!` erhöht man die Priorität seiner Forderung, man "zwingt" LaTeX zur Umsetzung.

## komplexere Tabelle mit zusätzlichen Paketen 

Um komplexere Tabellen zu erzeugen sind zusätzliche Pakete wie `booktabs` , `multirow` und `makecell` notwendig. Nachfolgend wir dies an einem Beispiel dargestellt:


````{tabbed} Beispiel 1 
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
````

````{tabbed} Beispiel 2
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
+ Verwendung des Pakets `booktabs` für `\toprule` , `\midrule` und `\bottomrule` (verbesserte horizontale Linien)
+ `@{}` am Anfang und  `@{}` am Ende in `\begin{tabular}{}` verkürzt die Tabelle links und rechts auf das nötigste
````

````{tabbed} Beispiel 3
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
+ `\multicolumn{1}{c}{Name}` um die Überschrift `Name` zu zentrieren obwohl die Spalte eigentlich linksausgerichtet ist
````

````{tabbed} Beispiel 4
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
+ `\multicolumn{2}{c}{Text}` fasst zwei Spalten zusammen (in dem Beispiel für die Überschrift)
````

````{tabbed} Beispiel 5
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
+ `\multirow{2}{*}{Name}` zentriert Name vertikal in dem es zwei Zeilen zusammenfuegt (durch Paket `multirow`) 
+ `\hfil` vor `\multirow` sorgt dafür das Name horizontal wieder zentriert wird
````

````{tabbed} Beispiel 6
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
+ mit `\textbf{}` kann die Überschrift zusätzlich hervorgehoben werden
````

````{tabbed} Beispiel 7
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
+ mit `\makecell[c]{text oben \\ text unten}` wurde ein Textumbruch innerhalb einer Zelle erzeugt (c=zentriert) (Paket `makecell`)
````

## Einheiten und Zahlenwerte in Tabellen

In dem Abschnitt zur Verwendung von Einheiten gibt es Beispiel zur Verwendung von Einheiten und Zahlen in Tabellen mit dem Paket `unitx`. Dabei werden die Zahlen automatisch gerundet und entsprechend dem Dezimantrenner ausgerichtet ([Link](Einfuehrung.html#Tabelle_mit_Einheiten)).


# Übung (Text, Abbildungen, Tabelle)

Um das nun gesehene selbst anzuwenden übertragen wir nun den Text, Abbildungen und die Tabelle von folgender Seite auf ein eigenes LaTeX Dokument:

[Der anthropogene Treibhauseffekt](https://www.klimanavigator.eu/dossier/artikel/011998/index.php)

Hinweise:
- Verwenden Sie `\label` und `\ref` für die Verweise auf die Abbildungen
- Erstellen Sie Bildunterschriften und Tabellenüberschriften


# Textformatierung

- fettgedruck: **fettgedruckter** Text wird mit dem `\textbf{...}` erzeugt
- kursiv: *kursiver* Text wird mit dem `\textit{...}` erzeugt
- unterstrichen: unterstrichener Text wird mit dem `\underline{...}` erzeugt

````{panels}
Input
^^^
```latex
Das ist ein \textbf{fettgedruckter Text} und das ein \textit{kursiver Text} und dieser \underline{Text ist unterstrichen}
```
---
Output
^^^
```{image} Einfuehrung/Textformatierung.png 
``` 
````

# Listen

Aufählungen werden in der `itemize`-Umgebung erzeugt. Ein Listeneinträge startet immer mit `\item`. Der Text kann eine beliebige Länge haben und der Textumbruch erfolgt automatisch sobald nicht wieder ein neuer Anstrich mit \verb|\item| erfolgt

````{panels}
Input
^^^
```latex
\begin{itemize}
  \item Eintrag 1
  \item Eintrag 2
  \item Eintrag 3
\end{itemize}
```
---
Output
^^^
```{image} Einfuehrung/item1.png 
:width: 150px
:align: center
``` 
````

Für Untereinträge wird jeweils eine neue `itemize`-Umgebung erzeugt

````{panels}
Input
^^^
```latex
\begin{itemize}
  \item Eintrag 1
  \begin{itemize}
   \item Untereintrag 1
   \item Untereintrag 2
   \item Untereintrag 3
  \end{itemize}
  \item Eintrag 2
  \item Eintrag 3
\end{itemize}
```
---
Output
^^^
```{image} Einfuehrung/item2.png
:width: 250px
:align: center
``` 
````

Nummerierte Auflistungen werden mit der `enumerate`-Umgebung analog erzeugt:

````{panels}
Input
^^^
```latex
\begin{enumerate}
  \item Eintrag 1
  \item Eintrag 2
  \item Eintrag 3
\end{enumerate}
```
---
Output
^^^
```{image} Einfuehrung/item3.png
:width: 150px
:align: center
``` 
````

Für Untereinträge erfolgen hier analog:

````{panels}
Input
^^^
```latex
\begin{enumerate}
  \item Eintrag 1
  \begin{enumerate}
   \item Untereintrag 1
   \item Untereintrag 2
   \item Untereintrag 3
  \end{enumerate}
  \item Eintrag 2
  \item Eintrag 3
\end{enumerate}
```
---
Output
^^^
```{image} Einfuehrung/item4.png
:width: 250px
:align: center
``` 
````


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






# Übung (mathematische Umbgeung)

**Aufgabe**

Gegeben ist eine Gleichung von Wikipedia ([https://de.wikipedia.org/wiki/Kontinuumsmechanik](https://de.wikipedia.org/wiki/Kontinuumsmechanik)). 

```{image} Einfuehrung/Untitled_13.png 
--- 
width: 500px 
align: center

``` 

Setzen Sie diese Gleichung ebenso in LaTeX.

**Lösung**

````{note} 
:class: dropdown
```latex
... globale Energiebilanz:
\[
\frac{\mathrm{d}}{\mathrm{d}t}\int_v\rho u\,\mathrm{d}v
+\frac{\mathrm{d}}{\mathrm{d}t}\int_v\frac{\rho}{2}\vec{v}\cdot\vec{v}\,\mathrm{d}v = 
\int_v\rho\vec{k}\cdot\vec{v}\,\mathrm{d}v 
+ \int_a\vec{t}\cdot\vec{v}\,\mathrm{d}a 
+ \int_v\rho r \,\mathrm{d}v 
-\int_a\vec{n}\cdot\vec{q}\,\mathrm{d}a \quad.
\]
```
```{image} Einfuehrung/Untitled_14.png 
--- 
width: 500px 
align: center
```
```` 

# Literaturverzeichnis

## Literaturverwaltung mit Zotero

Die HTWK Leipzig stellt für den Umgang mit Zotero selbst verschiedene [Tutorial-Videos zur Verfügung](https://bibliothek.htwk-leipzig.de/kurse-und-beratung/online-tutorials/online-zotero-kurs/).

## Einbindung der Literaturdatenbank in LaTeX

Hinweis: In Overleaf lässt auch direkt der Zotero-Account verknüpfen, so dass Overleaf die BiB-Datei immer automatisch aktualisiert, wenn sich etwas in Zotero ändert. Dies ist aber wohl nur für Premium-Nutzer von Overleaf verfügbar, so dass wir hier nicht darauf eingehen.

Ist die Datenbank in Zotero gefüllt, kann direkt aus der Bibliothek im Zotero eine BIBLaTeX-Datei erzeugt werden. Dazu unter `Datei` > `Bibliothek exportieren...` anklicken. Dann erhält man ein Dialogfenster:

```{image} Einfuehrung/Untitled_15.png 
--- 
width: 500px 
align: center
``` 

In diesem Fenter als Format `BibLaTeX` auswählen, mit OK bestätigen und dann die Bib-Datei im Ordner der LaTeX-Datei mit gewünschten Namen abspeichern (z.B. "mybib.bib").

## Literatur in LaTeX

Eine sehr gute Zusammenfassung zur Literatur in LaTeX gibt es in der [Overleaf Dokumentation (englisch)](https://de.overleaf.com/learn/latex/Bibliography_management_in_LaTeX). Im folgenden werden ein paar Grundlagen vermittelt:

Wir nutzen das Paket `BiBLaTeX`, die moderne Form der Literaturreferenzierung. Dazu muss man

- das Paket  `biblatex` laden
- die Bib-Datei einbinden mit `\addbibresource{name.bib}` (dort stehen alle Quellen drin)
- am Ende des Dokumentes das Literaturverzeichnis einbinden (mit Option im Inhaltsverzeichnis sichtbar zu machen) mit `\printbibliography[heading=bibintoc]`

Um erstmal anzufangen erstellen wir eine Beispiel Bib-Datei die auch in der Ovearleaf Dokumentation verwendet wird. In dieser sind 4 verschiedene Quellen eingetragen. Wir erzeugen eine Datei mit dem Namen `sample.bib` und fügen folgenden Inhalt ein:


````latex
@article{einstein,
    author = "Albert Einstein",
    title = "{Zur Elektrodynamik bewegter K{\"o}rper}. ({German})
    [{On} the electrodynamics of moving bodies]",
    journal = "Annalen der Physik",
    volume = "322",
    number = "10",
    pages = "891--921",
    year = "1905",
    DOI = "http://dx.doi.org/10.1002/andp.19053221004",
    keywords = "physics"
}

@book{dirac,
    title = {The Principles of Quantum Mechanics},
    author = {Paul Adrien Maurice Dirac},
    isbn = {9780198520115},
    series = {International series of monographs on physics},
    year = {1981},
    publisher = {Clarendon Press},
    keywords = {physics}
}

@online{knuthwebsite,
    author = "Donald Knuth",
    title = "Knuth: Computers and Typesetting",
    url  = "http://www-cs-faculty.stanford.edu/~uno/abcde.html",
    addendum = "(accessed: 01.09.2016)",
    keywords = "latex,knuth"
}

@inbook{knuth-fa,
    author = "Donald E. Knuth",
    title = "Fundamental Algorithms",
    publisher = "Addison-Wesley",
    year = "1973",
    chapter = "1.2",
    keywords  = "knuth,programming"
}
````

Der komplette Workflow wird nun an zwei verschiedenen Zitierstilen (`numeric` und `alphabetic`) dargestellt:






`````{tabbed} Stil=numeric
````{panels}
Input
^^^
```latex
\documentclass{article}

\usepackage[
backend=biber,
style=numeric,
sorting=none
]{biblatex} % Literatur-Paket mit Einstellungen
\usepackage[ngerman]{babel} % deutsches Sprachpaket
\addbibresource{sample.bib} % import Bib-Datei

\begin{document}

Quelle1 (Einstein) \cite{einstein} ... Quelle2 (Dirac) \cite{dirac} ... Quelle1 (Einstein) noch mal  \cite{einstein} ... Quelle3 (Knuth) \cite{knuthwebsite}

\printbibliography % Literaturverzeichnis einfügen

\end{document}
```
---
Output
^^^
```{image} Einfuehrung/Bib_numeric.png
:width: 300px
:align: center
``` 
__________________________________
- mit \cite{label} wird die Quelle zitiert
- Einstellungen im Paket `biblatex`
    - `style=numeric` numerischer Stil (Quellen mit Zahl indiziert)
    - `sorting=none` Sortierung nach Verwendung im Literaturverzeichnis
````
`````

`````{tabbed} Stil=alphabetic
````{panels}
Input
^^^
```latex
\documentclass{article}

\usepackage[
backend=biber,
style=alphabetic,
sorting=nyt
]{biblatex} % Literatur-Paket mit Einstellungen
\usepackage[ngerman]{babel} % deutsches Sprachpaket
\addbibresource{sample.bib} % import Bib-Datei

\begin{document}

Quelle1 (Einstein) \cite{einstein} ... Quelle2 (Dirac) \cite{dirac} ... Quelle1 (Einstein) noch mal  \cite{einstein} ... Quelle3 (Knuth) \cite{knuthwebsite}

\printbibliography % Literaturverzeichnis einfügen

\end{document}
```
---
Output
^^^
```{image} Einfuehrung/Bib_alphabetic.png
:width: 300px
:align: center
``` 
__________________________________
- mit \cite{label} wird die Quelle zitiert
- Einstellungen im Paket `biblatex`
    - `style=alphabetic` alphabetischer Stil (Quellen mit Autornamen und Jahr indiziert, hilft dem Leser die Quellen besser zuzuordnen ohne ins Literaturverzeichnis zu schauen)
    - `sorting=nyt` Sortierung nach Name, Jahr und Titel im Literaturverzeichnis
````
`````

Nur die Quellen aus der Bib-Datei die mit `\cite{}` referenziert werden, werden auch im Literaturverzeichnis dargestellt. Die Bib-Datei kann dabei also auch viel größer sein und nicht verwendete Quellen werden einfach nicht angezeigt.

Um mehrere Quellen (z.B. label1, label2 und label3) zu zitieren werden diese per Komma in `\cite{label1,label2,label3}` Befehl getrennt:

````{panels}
Input
^^^
```latex
Mehrere Quellen \cite{einstein,dirac,knuth-fa} 
```
---
Output
^^^
```{image} Einfuehrung/Bib_numeric2.png
:width: 300px
:align: center
``` 
````

Um auf eine bestimmte Seite innerhalb der Quelle zu referenzieren kann dies mit eckigen Klammern als Option an den `\cite[]{}` Befehl verwendet werden:

````{panels}
Input
^^^
```latex
siehe \cite[S. 6]{dirac} 
```
---
Output
^^^
```{image} Einfuehrung/Bib_numeric3.png
:width: 300px
:align: center
``` 
````


Um das Literaturverzeichnis im Inhaltsverzeichnis anzuzeigen gibt es eine Option im Befehl `\printbibliography` :

```latex
\printbibliography[heading=bibintoc]
```

Zusätzlich können mit dem Befehl `\ExecuteBibliographyOption{}` Einstellungen vorgenommen werden um z.B. ISBN und URLs zu deaktivieren:

```latex
\usepackage[
backend=biber,
style=numeric,
sorting=none
]{biblatex}
\ExecuteBibliographyOptions{
isbn=false, %keine isbn anzeigen
url=false %keine url anzeigen
}
```

Die Option `url=false` zeigt weiterhin alle Quellen an die mit `@online` gekennzeichnet sind. Wenn man jedoch den Typ `Webseite` von **Zotero** exportiert, wird dieser als Typ `@misc` umgewandelt und die URL wird nicht mit ausgegeben. Folgender Code vom [User mit dem Namen moewe von stackexchange.com](https://tex.stackexchange.com/a/429112) kann in LaTeX eingefügt werden um den Typ `@misc` in Typ `@online` zu ändern, vorrausgesetzt man hat keine Quelle die wirklich als `@misc` gekennzeichnet werden sollte:

```latex
\DeclareSourcemap{
  \maps[datatype=bibtex, overwrite=true]{
    \map{
      \step[typesource=misc, typetarget=online]
    }
  }
}
```

Noch mehr Informationen finden sich in der [offizielen Dokumentation zum Paket biblatex](http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/biblatex/doc/biblatex.pdf).