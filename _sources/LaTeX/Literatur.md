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