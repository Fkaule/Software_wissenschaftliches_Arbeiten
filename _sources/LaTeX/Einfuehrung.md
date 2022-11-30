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

::::{grid}

:::{grid-item-card} Input

```latex
\documentclass{article}
\begin{document}
    Hallo Welt.
\end{document}
```

:::

:::{grid-item-card} Output

```{image} Einfuehrung/Untitled.png

```

:::

::::
