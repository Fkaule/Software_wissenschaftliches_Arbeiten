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
