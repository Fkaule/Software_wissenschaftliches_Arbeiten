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
``` 
````


# Mathematische Umgebungen

- Verwendung von Formelzeichen durch Einbettung mit `$` Zeichen: z.B. `$\alpha$`
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
- `\sin()` ,  `\cos()` ...
- Brüche mit `\frac{}{}`
- hochstellen mit `^`
- tiefstellen mit `_`
- Zahlen mit Einheiten mit `\mathrm{}` und halbes Leerzeichen `\,` und Komma mit `{,}` eingrenzen  also z.B. `15{,}4\,\mathrm{mm}`

[Zahlen und Einheiten](https://tobiw.de/tbdm/siunitx)