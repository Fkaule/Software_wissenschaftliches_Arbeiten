# Einfuehrung

## Links

[Documentation](https://www.overleaf.com/learn/latex/Main_Page)

## Nutzung und Installation

Es gibt für LaTeX mittlerweile zwei prinzipielle Möglichkeiten:

- online im Webbrowser

    [Overleaf, Online LaTeX Editor](https://www.overleaf.com/)

- Installation auf dem eigenen Rechner
    - Windows

        [Home - MiKTeX.org](https://miktex.org/)

    - Mac

        [MacTeX - TeX Users Group](https://tug.org/mactex/)

    - Linux

        [ubuntuusers.de](https://wiki.ubuntuusers.de/TeX_Live/)

Für uns ist im Moment die Nutzung online am einfachsten und sehr direkt umsetzbar. Daher bitte bei overleaf einen Account (kostenlos) anlegen. Dann kann es losgehen ...

## Ein erstes "Hallo Welt"

```latex
\documentclass{article}

\begin{document}
    Hallo Welt.
\end{document}
```

```{figure} Einfuehrung/Untitled.png 
--- 
width: 500px 
name: Untitled
--- 
caption 
``` 

### \documentclass - Dokumentklassen

`article` - für kleinere Texte, beinhaltet keine Kapitelüberschriften

`report` - Berichte, Abschlussarbeiten, beinhaltet Kapitelüberschriften

`book` - umfangreiche Texte, beinhaltet Kapitelüberschriften und ist standardmäßig zweiseitig

Es gibt ähnliche Klassen, die zum modernen und weitverbreiteten KOMA-Skript gehören. Diese lauten dann:

`scrartcl`

`scrreprt`

`scrbook`

Wir werden im weiteren Verlauf vor allem auf `scrreprt` setzen, da diese Klasse nahe einer Abschlussarbeit kommt und damit gut zu uns passt.

Es gibt noch weitere Klassen zum Schreiben von Briefen (dinbrief) o.ä., die wir hier aber nicht genauer betrachten wollen. Ist der Einstieg in LaTeX geschafft, kann man diese auch schnell selbst einbinden.

## Dokumentstruktur

### Seitenränder

TODO

### Absätze und Zeilenumbrüche

Absätze dienen der Struktur des Fließtextes. Sie sind das einzige Mittel, um Fließtext umzubrechen. Manuelle Zeilenumbrüche führen zu schlechten Textbildern.

### Überschriftsebenen

- es gibt maximal drei nummerierte Ebenen für die Dokumentstruktur
- article-Klassen:

```latex
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```

```{figure} Einfuehrung/Untitled_1.png 
--- 
width: 500px 
name: Untitled_1
--- 
caption 
``` 

- report/book-Klassen:

```latex
\chapter{Kapitelüberschrift}
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```

```{figure} Einfuehrung/Untitled_2.png 
--- 
width: 500px 
name: Untitled_2
--- 
caption 
``` 

### Inhaltsverzeichnis

```latex
\begin{document}

%...

\tableofcontents % Inhaltsverzeichnis
\listoffigures % Abbildungsverzeichnis
```

```{figure} Einfuehrung/Untitled_3.png 
--- 
width: 500px 
name: Untitled_3
--- 
caption 
``` 

```{figure} Einfuehrung/Untitled_4.png 
--- 
width: 500px 
name: Untitled_4
--- 
caption 
``` 

weiter unten noch etwas mehr dazu ... 

## Bilder einfügen

### Allgemeines

Das Einfügen von Bildern ist in LaTeX besonders einfach und ungewohnt (wenn man Word gewohnt ist) zugleich. **EINFACH** - da LaTeX die Aufgabe übernimmt, das Bild vernünftig zum Text zu positionieren. **UNGEWOHNT** - da LaTEX die Aufgabe übernimmt, das Bild vernünftig zum Text zu positionieren. Daher der Rat: Erzwingen Sie nichts, sondern vertrauen Sie LaTeX.

Generell gilt für eine gute Bildposition im wissenschaftlichen Text:

- Bilder werden nicht vom Text umflossen, sondern nehmen als Objekt die gesamte Textbreite ein
- Bilder sollten am unteren oder oberen Rand der Seite positioniert werden, um den Textfluss nicht zu stören.
- Bilder sollten, wenn möglich, die Textbreite nutzen. Eventuell auch mehrere Bilder in einer Abbildungsumgebung unterbringen, wenn es inhaltlich sinnvoll ist.

    ```latex
    \documentclass...

    \usepackage{graphicx} % Grafiken einbinden

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

    ```

```{figure} Einfuehrung/Untitled_5.png 
--- 
width: 500px 
name: Untitled_5
--- 
caption 
``` 

Die Befehle `\label` und `\ref` dienen hier zur Referenzierung des Bildes. Es wird ein eindeutiges Label vergeben, welches dann überall im Text als Referenz wieder abgerufen werden kann. Dieser Mechanismus gilt nicht für Abbildungen, sondern auch Tabellen, Gleichungen, etc.

Mit der Positionsangabe `[!h]` kann man LaTeX Hinweise zu den Positionswünschen übermitteln. Möglich sind:

- `h` - here - bitte versuche es genau an dieser Textstelle
- `t` - top - wenn möglich an Oberkante der Seite
- `b` - bottom - wenn möglich, an Unterkante der Seite
- `p` - page - nutze eine extra Seite für die Bilder

Mit dem `!` erhöht man die Priorität seiner Forderung, man "zwingt" LaTeX zur Umsetzung.

### Bilderunterschriften in schick

Natürlich kann man in LaTeX auch Dinge anpassen. Beispielsweise die Bildbeschriftung lässt sich über ein zusätzliches Package "caption" einstellen:

```latex
...
\usepackage{caption}
\captionsetup{labelfont=bf,font=small,textfont=it}
...
\begin{document}
...
```

vorher:

```{figure} Einfuehrung/Untitled_6.png 
--- 
width: 500px 
name: Untitled_6
--- 
caption 
``` 

nachher (mit caption-Package):

```{figure} Einfuehrung/Untitled_7.png 
--- 
width: 500px 
name: Untitled_7
--- 
caption 
``` 

### Bilder mit LaTeX-Schrift (mit `.pdf_tex`)

Verwendet man Vektorgrafiken als Bildformate, z.B. für Skizzen/Schemata, werden diese über das PDF-Dateiformat eingebunden. Dabei sind die Vorteile, dass 

- die Bilder frei skalierbar sind, ohne unscharf zu werden und
- man im Prinzip auf jedes grafische Element zugreifen kann.

Verwendet man Inkscape als Grafikprogramm, lassen sich aus den SVG-Dateien auch PDFs abspeichern. Dabei kann man im Speicherdialog die Textausgabe in eine LaTeX-Datei umleiten:

```{figure} Einfuehrung/Untitled_8.png 
--- 
width: 500px 
name: Untitled_8
--- 
caption 
``` 

**Beispiel:**

In Inkscape wurde die folgende Skizze erstellt (Dokumentgröße wurde mit 100mm x 100mm definiert):

- der Text hier ist als normaler Text eingefügt, wobei gleich die LaTeX-Notation für mathematische Zeichen angegeben wird
- der Text ist entsprechend eingefärbt, um die Bedeutung klarer zu machen (dies wird dann so übernommen)
- beim Abspeichern als PDF mit LaTeX-Ausgabe entstehen zwei Dateien:
    - *Skizze.pdf* (die eigentliche Skizze)
    - *Skizze.pdf_tex* (LaTeX-Datei mit Schrift und Einbindung der PDF)

```{figure} Einfuehrung/Untitled_9.png 
--- 
width: 500px 
name: Untitled_9
--- 
caption 
``` 

Das Bild wollen wir in LaTeX einbinden, so wie es erstellt wurde:

```latex
...
\usepackage{color} %Nutzung von Farbe
...
\begin{figure}[!h]
    \centering
    \input{Skizze.pdf_tex}
    \caption{Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.}
    \label{fig:skizze}
\end{figure}
...
```

```{figure} Einfuehrung/Untitled_10.png 
--- 
width: 500px 
name: Untitled_10
--- 
caption 
``` 

⇒ die Schrift wurde durch LaTeX-Schrift, wie sie im Dokument verwendet wird, ersetzt

Im nächsten Schritt wollen die Stärken dieses Vorgehens demonstrieren:

- das Bild wird in unterschiedlichen Größen nebeneinander eingefügt
- das Bild ist frei skalierbar (hier Verkleinerung auf `0.4\textwidth`), ohne Verluste
- die Schrift bleibt so groß, wie das Dokument es vorgibt und wird nicht mit skaliert (immer lesbar!)

```latex
...
\usepackage{color} %Nutzung von Farbe
...
\begin{figure}[!h]
    \centering
    \def\svgwidth{0.35\textwidth} % erstes Bild
    \input{Skizze.pdf_tex}
    \def\svgwidth{0.55\textwidth} % zweites Bild
    \input{Skizze.pdf_tex}
    \caption{Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.}
    \label{fig:skizze}
\end{figure}
```

```{figure} Einfuehrung/Untitled_11.png 
--- 
width: 500px 
name: Untitled_11
--- 
caption 
``` 

⇒ das Bild wurde deutlich verkleinert, die Schrift bleibt genauso groß, wie es vom Dokument vorgegeben wird

### Bilder mit LaTeX-Schrift (mit `.svg`)

Analog können auch Inkscape-Grafiken mit der Dateiendung `.svg` direkt in LaTeX verwendet werden dafür ist folgender Code notwendig:

```latex
...
\usepackage{svg} %Einbindung von svg Grafiken
...
\begin{figure}[!h] 
    \centering
    \includesvg[width=120mm]{Beispiel.svg}
    \caption{Beispiel Vektorgrafik mit LaTeX rendering}
    \label{fig:Beispiel_Vektor}
\end{figure}
```

## Übung zur LaTeX-Schrift in Bildern

**Aufgabe**

Gegeben ist die folgende Grafik als PNG-Datei. Diese kann man einfach einbinden mit `\includegraphics{...}`.

```{figure} Einfuehrung/Skizze-Ubungsbild.png 
--- 
width: 500px 
name: Skizze-Ubungsbild
--- 
caption 
``` 

Nutzen Sie bitte die SVG-Datei dazu im Inkscape und setzen Sie die Beschriftung neu mit Text, den Sie dann im LaTeX-Dokument wieder ersetzen!

```{admonition} Für die Lösung auf den Button klicken zum aufklappen
:class: dropdown

![](Einfuehrung/Loesung_InkscapeLaTeX.png)
```


## Tabellen

Zugegeben, Tabellen sind nicht so einfach zu erstellen in LaTeX. Es ist weniger die Schwierigkeit, als mehr der Aufwand, den sie beim erstellen erzeugen. Aber es geht:

```latex
... sunt in culpa qui officia deserunt mollit anim id est laborum (s. Tabelle \ref{tab:test}).
%
\begin{table}[h]
    \centering
    \caption{Tabellenbeschriftung}
    
		\begin{tabular}{|l|r|r|}
    \hline
       awort  & cwörter mehr & das ist ein test.\\
       \hline
       bwort  & dwörter mehr & das ist ein test.\\
       \hline
    \end{tabular}
    
    \label{tab:test}
\end{table}
```

```{figure} Einfuehrung/Untitled_12.png 
--- 
width: 500px 
name: Untitled_12
--- 
caption 
``` 

## Mathematische Umgebungen

- Verwendung von Formelzeichen durch Einbettung mit $ Zeichen: z.B. $\alpha$

- Gleichungen zwischen `\begin{equation}` und `\end{equation}`  

```latex
\begin{equation}
    f(x,\mu,\sigma^2)=\frac{1}{\sqrt{2\pi \sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
    \label{equ:glg1}
\end{equation}
```
Mathematische Objekte:

- griechische Buchstaben z.B. `\alpha` oder pi mit `\pi`
- Quadratwurzel `\sqrt{}` .. kubische Wurzel `\sqrt[3]{}`
- `\sin()` ,  `\cos()` ...`
- Brüche mit `\frac{}{}`
- hochstellen mit `^`
- tiefstellen mit `_`
- Zahlen mit Einheiten mit `\mathrm{}` und halbes Leerzeichen `\,` und Komma mit `{,}` eingrenzen  also z.B. `15{,}4\,\mathrm{mm}`

[Zahlen und Einheiten](https://tobiw.de/tbdm/siunitx)

### Übungen

**Aufgabe**

Gegeben ist eine Gleichung von Wikipedia ([https://de.wikipedia.org/wiki/Kontinuumsmechanik](https://de.wikipedia.org/wiki/Kontinuumsmechanik)). 

```{figure} Einfuehrung/Untitled_13.png 
--- 
width: 500px 
name: Untitled_13
--- 
caption 
``` 

Setzen Sie diese Gleichung ebenso in LaTeX.

**Lösung**

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

```{figure} Einfuehrung/Untitled_14.png 
--- 
width: 500px 
name: Untitled_14
--- 
caption 
``` 

## Literaturverzeichnis

### Literaturverwaltung mit Zotero

Die HTWK Leipzig stellt für den Umgang mit Zotero selbst verschiedene Tutorial-Videos zur Verfügung:

[](https://bibliothek.htwk-leipzig.de/kurse-und-beratung/online-tutorials/online-zotero-kurs/)

### Einbindung der Literaturdatenbank in LaTeX

Hinweis: In Overleaf lässt auch direkt der Zotero-Account verknüpfen, so dass Overleaf die BiB-Datei immer automatisch aktualisiert, wenn sich etwas in Zotero ändert. Dies ist aber wohl nur für Premium-Nutzer von Overleaf verfügbar, so dass wir hier nicht darauf eingehen.

Ist die Datenbank in Zotero gefüllt, kann direkt aus der Bibliothek im Zotero eine BIBLaTeX-Datei erzeugt werden. Dazu unter `Datei > "Bibliothek exportieren...`" anklicken. Dann erhält man ein Dialogfenster:

```{figure} Einfuehrung/Untitled_15.png 
--- 
width: 500px 
name: Untitled_15
--- 
caption 
``` 

In diesem Fenter als `Format "BibLaTeX"` auswählen, mit OK bestätigen und dann die Bib-Datei im Ordner der LaTeX-Datei mit gewünschten Namen abspeichern (z.B. "mybib.bib").

### Literatur in LaTeX

Es gibt verschiedene Literatur-Systeme in LaTeX. Wir nutzen BiBLaTeX, die moderne Form der Literaturreferenzierung. Dazu muss man

- das Package  `biblatex`laden
- die Bib-Datei einbinden mit `\addbibresource`
- am Ende des Dokumentes das Literaturverzeichnis einbinden (mit Option im Inhaltsverzeichnis sichtbar zu machen) mit `\printbibliography[heading=bibintoc]`

```latex
...
\usepackage{biblatex}
\addbibresource{mybib.bib}

...
Text ... \cite{abcd} ... Text
...
\printbibliography[heading=bibintoc]

\end{document}
```

Dann kann man mit `\cite{KEY}` die Literaturreferenzen einfügen. Dabei ist der KEY der verwendete Schlüssel in der Bib-Datei. Dieser steht immer ganz oben im Bib-Eintrag (hier im Beispiel farblich markiert):

```latex
@article{wallburg_material_2019,
	title = {Material Removal Simulation in Sawing Processes of Photovoltaic Silicon},
	volume = {4},
	rights = {All rights reserved},
	issn = {2059-8521},
	url = {https://www.cambridge.org/core/product/identifier/S2059852119000951/type/journal_article},
	doi = {10.1557/adv.2019.95},
	abstract = {...},
	pages = {761--768},
	number = {13},
	journaltitle = {{MRS} Advances},
	shortjournal = {{MRS} Adv.},
	author = {Wallburg, F. and Kuna, M. and Schoenfelder, S.},
	urldate = {2019-08-13},
	date = {2019},
	langid = {english},
	file = {Wallburg et al. - 2019 - Material Removal Simulation in Sawing Processes of.pdf:.../Wallburg et al. - 2019 - Material Removal Simulation in Sawing Processes of.pdf:application/pdf}
}
```

Zitierung [1,2] und nicht [1][2]

TODO

## Verzeichnisse

### Symbolverzeichnis

TODO

## Titlepage

[Customising Your Title Page and Abstract](https://www.overleaf.com/learn/latex/How_to_Write_a_Thesis_in_LaTeX_(Part_5):_Customising_Your_Title_Page_and_Abstract)

## Befehle definieren

Todo