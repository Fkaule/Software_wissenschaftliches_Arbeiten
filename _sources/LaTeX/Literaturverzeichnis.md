# Literaturverzeichnis

## Literaturverwaltung mit Zotero

Die HTWK Leipzig stellt für den Umgang mit Zotero selbst verschiedene Tutorial-Videos zur Verfügung:

[](https://bibliothek.htwk-leipzig.de/kurse-und-beratung/online-tutorials/online-zotero-kurs/)

## Einbindung der Literaturdatenbank in LaTeX

Hinweis: In Overleaf lässt auch direkt der Zotero-Account verknüpfen, so dass Overleaf die BiB-Datei immer automatisch aktualisiert, wenn sich etwas in Zotero ändert. Dies ist aber wohl nur für Premium-Nutzer von Overleaf verfügbar, so dass wir hier nicht darauf eingehen.

Ist die Datenbank in Zotero gefüllt, kann direkt aus der Bibliothek im Zotero eine BIBLaTeX-Datei erzeugt werden. Dazu unter `Datei > "Bibliothek exportieren...`" anklicken. Dann erhält man ein Dialogfenster:

```{image} Einfuehrung/Untitled_15.png 
--- 
width: 500px 
align: center
``` 

In diesem Fenter als `Format "BibLaTeX"` auswählen, mit OK bestätigen und dann die Bib-Datei im Ordner der LaTeX-Datei mit gewünschten Namen abspeichern (z.B. "mybib.bib").

## Literatur in LaTeX

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
