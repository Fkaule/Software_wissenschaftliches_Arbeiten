# Gliederung und Verzeichnisse

## Überschriftsebenen

Es gibt maximal drei nummerierte Ebenen für die Dokumentstruktur:

**article-Klassen** `\documentclass{article}`:

::::{grid}

:::{grid-item-card} Input
```latex
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```
:::

:::{grid-item-card} Output
```{image} Einfuehrung/Untitled_1.png 
``` 
:::

::::




**report/book-Klassen** `\documentclass{report}` oder `\documentclass{book}`:

::::{grid}

:::{grid-item-card} Input
```latex
\chapter{Kapitelüberschrift}
\section{Überschrift}
\subsection{Unterüberschrift}
\subsubsection{Unterunterüberschrift}
\paragraph{Letzte Chance}
```
:::

:::{grid-item-card} Output
```{image} Einfuehrung/Untitled_2.png 
``` 
:::

::::

## Inhaltsverzeichnis

- Innerhalb von `\begin{document}` und `\begin{document}` : 

::::{grid}

:::{grid-item-card} Input
```latex
\tableofcontents % Inhaltsverzeichnis
```
:::

:::{grid-item-card} Output
```{image} Einfuehrung/Untitled_3.png 
``` 
:::

::::

## Abbildungsverzeichnis

- Innerhalb von `\begin{document}` und `\begin{document}` : 


::::{grid}

:::{grid-item-card} Input
```latex
\listoffigures % Abbildungsverzeichnis
```
:::

:::{grid-item-card} Output
```{image} Einfuehrung/Untitled_4.png 
``` 
:::

::::