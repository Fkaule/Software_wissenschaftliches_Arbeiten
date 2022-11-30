# Listen

Aufählungen werden in der `itemize`-Umgebung erzeugt. Ein Listeneinträge startet immer mit `\item`. Der Text kann eine beliebige Länge haben und der Textumbruch erfolgt automatisch sobald nicht wieder ein neuer Anstrich mit \verb|\item| erfolgt

::::{grid}
:::{grid-item-card} Input

```latex
\begin{itemize}
  \item Eintrag 1
  \item Eintrag 2
  \item Eintrag 3
\end{itemize}
```

:::
:::{grid-item-card} Output

```{image} Einfuehrung/item1.png
:width: 150px
:align: center
```

:::
::::

Für Untereinträge wird jeweils eine neue `itemize`-Umgebung erzeugt

::::{grid}
:::{grid-item-card} Input

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

:::
:::{grid-item-card} Output

```{image} Einfuehrung/item2.png
:width: 250px
:align: center
```

:::
::::

Nummerierte Auflistungen werden mit der `enumerate`-Umgebung analog erzeugt:

::::{grid}
:::{grid-item-card} Input

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

:::
:::{grid-item-card} Output

```{image} Einfuehrung/item4.png
:width: 250px
:align: center
```

:::
::::
