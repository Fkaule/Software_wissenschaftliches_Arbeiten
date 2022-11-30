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

Innerhalb der `document`-Umgebung (nach `\begin{document}`) können Bilder eingefügt werden. Dafür wird eine `figure`-Umgebung erstellt (mit `\begin{figure}` und `\end{figure}`). Innerhalb dieser Umgebung kann dann mit \includegraphics{bild.png} z.B. eine Datei `bild.png` eingefügt werden. Konkret wird dies am nachfolgenden Beispiel verdeutlicht:

::::{grid}
:::{grid-item-card} Input

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

:::
:::{grid-item-card} Output

```{image} Einfuehrung/Untitled_5.png

```

:::
::::

<br>
Nachfolgend nun die Erklärungen zu den Befehlen:

## Referenzierungen

- `\label{label_name}` (innerhalb von der `figure`-Umgebung) erstellt ein label welches im Text (also außerhalb der `figure`-Umgebung) mit dem Befehl `\ref{label_name}` referenziert werden kann. Es wird dann die zugehörige Nummer eingefügt.
- `\includegraphics[width=60mm]{dependency.png}` wird die Bilddatei `dependency.png` mit einer Breite von 60mm eingefügt. Die Datei liegt dabei im gleichen Verzeichnis wie die LaTeX Datei, es sind aber auch relative Pfade möglich (z.B. in einen Ordner Abbildungen `\includegraphics{Abbildungen/dependency.png}`). Es können Bilder mit der Dateieindung `.png` , `.jpg` und `.jpeg` standardmäßig verwendet werden.

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

::::{tab-set}

:::{tab-item} Bildunterschrift Standard

```{image} Einfuehrung/Untitled_6.png

```

:::
:::{tab-item} Bildunterschrift verbessert (mit caption-Paket)

```{image} Einfuehrung/Untitled_7.png

```

:::

::::

## Mehrere Abbildungen in einer Figure Umgebung (subfigure)

Es gibt verschiedene Variante wie man mehrere Bilder in einer `figure`-Umgebung platzieren kann. Hier ein Beispiel in dem das Paket `subcaption` benutzt wird und die Bilder in einer `\subcaptionbox` erstellt werden:

::::{tab-set}

:::{tab-item} ohne `/hfill`

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

:::

:::{tab-item} mit `/hfill`

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
  :::

::::
