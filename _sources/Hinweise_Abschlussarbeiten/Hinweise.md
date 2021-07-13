# Hinweise zum Schreiben von Abschlussarbeiten


## Vorwort

Abschlussarbeiten wie Bachelorarbeit oder Masterarbeit (oder auch Projektarbeiten) sind Dokumentationen der eigenen wissenschaftlichen Arbeit, der Bearbeitung der Aufgabe. Dabei wird entsprechend wissenschaftlicher Regeln dokumentiert. In diesen Text sollen dazu einige Hinweise erfolgen.

Die hier vorgestellten Hinweise und Anleitungen beziehen sich vor allem auf meine jahrelange persönliche Erfahrungen mit der Dokumentation von wissenschaftlichen Arbeiten. Es erfüllt nicht den Anspruch auf Vollständigkeit. Weiterhin gibt es im Einzelfall sicher auch unterschiedliche Meinungen, wie man in der Zeit an der Hochschule aber auch im späteren Berufsleben feststellen wird. Dennoch würde ich meine Aussagen hier als guten Ausgangspunkt sehen, um eine sehr gute Arbeit zu schreiben.

Leipzig, April 2020

---

## Software

Den meisten Student*innen sind die Produkte von Microsoft, also Word, Excel, Powerpoint, bekannt. Natürlich kann damit die Arbeit erstellt werden. Allerdings gibt es da durchaus noch mehr Möglichkeiten, mit besseren Funktionen, gerade für wissenschaftliche Arbeiten. Bevor man also die Wahl der zu verwendenden Tools trifft, sind man diese kennen.

Alle folgenden Empfehlungen sind "Open Source" Lösungen, die frei installiert und verwendet werden können. Dies macht es insbesondere für die studentische Nutzung interessant.

### Textverarbeitung - LaTeX

Für das Verfassen längerer Texte bietet sich LaTeX (gesprochen LateCH, da der letzte Buchstabe ein griechisches Chi darstellt) an. Dabei handelt es sich um eine Markup language, ähnlich wie HTML, in der man den Text als einfaches Textdokument mit entsprechenden Befehlen "programmiert". Dies macht es am Anfang etwas umständlicher im Umgang. Aber mit etwas Übung lässt sich so genauso schreiben, wie mit anderen Programmen.

Für den Einstieg ist die webbasierte LaTeX-Umgebung [www.overleaf.com](http://www.overleaf.com) zu empfehlen. Man kann sich kostenfrei registrieren und ohne Installation und viel Hilfe und Vorlagen einarbeiten. Auch eine Installation auf den eigenen Rechner kann für alle Plattformen, Win, Mac, Linux, erfolgen.

[➡️ Kurs: Texte mit LaTeX](../LaTeX/LaTeX_Uebersicht.md)

### Literaturverzeichnis

Jede Arbeit muss darüber ihre Referenzen benennen. In den Ingenieurwissenschaften sind dies Bücher, Abschlussarbeiten, Artikel, Webseiten. Mit letzteren bitte nicht übertreiben. Es empfiehlt sich, bereits bei der Literaturrecherche eine Datenbank anzulegen. Diese Datenbank ist dann die Grundlage für die Referenzen im Textdokument. Dafür gibt es verschiedene Lösungen wie Citavi, [Jabref](http://www.Jabref.org) oder [Zotero](http://www.Zotero.org). Die beiden zuletzt genannten sind frei verfügbar. Für Citavi gibt es eine Lizenz der Hochschule.

In Verbindung mit LaTeX haben vor allem Jabref und Zotero gute Schnittstellen über bibtex, Literatureinbindung in Latex, so dass direkt aus der Datenbank im Dokument referenziert werden kann. Das Literaturverzeichnis wird dann automatisch zusammengestellt und angefügt. Fairerweise sei erwähnt, dass es auch Plugins für Word gibt, die den gleichen Job ziemlich gut machen.

[➡️ Kurs: Literatur mit Zotero](../Zotero/Zotero_Uebersicht.md)


### Bilder und Diagramme

"Ein Bild sagt mehr als 1000 Worte" - wer kennt das nicht. Tatsächlich ist es für Ingenieure aber sehr wichtig, die oft sehr komplexen Zusammenhänge in vernünftigen Darstellungen (Skizzen, Schematas) darzustellen, um Leser*innen schnell die Konzepte bzw. Ergebnisse zu vermitteln. Dabei stellt man oft fest, dass in studentischen Arbeiten kaum eigene Skizzen erstellt werden. Hierfür gibt es aber sehr geeignete Software: [Inkscape](http://www.inkscape.org). Die Anwendung bedarf etwas Übung, aber man wird schnell dazulernen. Weiterhin ist das Internet dazu voll von Lösungen zu bestimmten Fragen.

[➡️ Kurs: Grafiken mit Inkscape](../Inkscape/Inkscape_Uebersicht.md)


Ein anderer Punkt sind Diagramme. Diese sind häufig die einzige Möglichkeit, die Ergebnisse darzustellen. Sehr umfangreiche Möglichkeiten bietet dazu **Python** Bibliothekn wie [**matplotlib**](https://matplotlib.org/) oder [**seaborn**](http://seaborn.pydata.org/), ein skriptbasiertes Tool, welches vor allem Daten in Form von ASCII-Dateien (.txt, .csv, ...) einfach und schnell verarbeiten kann und eine Grafik als PDF, PNG, JPG, ... erzeugen kann. Mit Python können auch Funktionen gefittet werden und vieles, vieles mehr. Man kann aber erst einmal klein anfangen.

[➡️ Kurs: Datenvisualisierung mit Python](../Python/Python_Uebersicht.md)


---

## Formatierung

Es gibt in wissenschaftlichen Arbeiten sehr verschiedene Möglichkeiten der Darstellung. Dabei sollen hier nicht die Feinheiten der Randabstände vorgegeben werden, sondern vielmehr einige grundsätzliche Dinge angesprochen werden, die es zu beachten gilt.

### Layout
<a id='Layout'></a>

#### Allgemein
<a id='Allgemein'></a>

Zum Layout der Arbeiten gibt es häufig Vorlagen/Vorgaben. Ohne Details festlegen zu wollen, ist generell zu empfehlen:

- sauberes Deckblatt mit Logos der Hochschule (und Unternehmen) sowie der notwendigen Informationen
- vernünftige Seitenränder (2-3cm) die ein gutes Gesamtbild der A4-Seite ergeben
- vernünftige Schriftgrößen (Times 12pt, Arial 11pt) mit ca. 1,5-zeiligen Abstand, klarer Abstand zwischen Absätzen bzw. Einzug der ersten Zeile beim Abstand (s. Beispiel)
- sauberes Schriftbild: keine farbigen Überschriften, nicht übertreiben mit fett und kursiv im Fließtext, seriös und sachlich
- Seitenzahlen in der Fußzeile
- Verzeichnisse: 
Inhalt - Pflicht, 
Abbildungs- und Tabellenverzeichnisse optional, 
Symbolverzeichnis wenn notwendig
- Gliederungsebenen im Inhaltsverzeichnis: Es gib maximal drei nummerierte Ebenen und eine vierte nicht nummerierte Ebene von Überschriften. Es wird maximal bis zu dritten Ebene im Inhaltsverzeichnis dargestellt.
    - Beispiel



```{figure} Hinweise/Untitled_1.png 
--- 
width: 500px 
name: Untitled_1
--- 
Text mit Überschriften 
``` 

```{figure} Hinweise/Untitled.png 
--- 
width: 500px 
name: Untitled
--- 
Literaturverzeichnis zum Text 
``` 

### Rechtschreibung und Ausdruck
<a id='Rechtschreibung_Ausdruck'></a>

In der deutschen Sprache haben wir uns auf einige Regeln verständigt und diese im Duden zusammengefasst. Auch wenn es die allgemeine Auffassung gibt, dass Ingenieur*innen vor allem den technischen und weniger den sprachlichen Sachverstand mitbringen, möchte ich hier feststellen, dass dies Quatsch ist. Auch in den Ingenieurwissenschaften muss man in der Lage sein, Texte sauber, orthografisch richtig und mit einem passenden Ausdruck zu verfassen. Wie alles bedarf auch das der Übung, je nach eigener Begabung in unterschiedlichem Maße. Dazu folgende Punkte, die mir immer wieder auffallen: 

- Man schreibt im Fließtext und unterteilt diesen in **Absätze**. Die Absätze fassen Sätze zum gleichen Gedanken, zum gleichen Thema zusammen. Wechselt das Thema, beginnt ein neuer Absatz. Aber nicht nach jedem einzelnen Satz! Und auch nicht erst nach drei Seiten!
Faustregel für eine Absatzlänge:
    - Ein Absatz besteht aus mindestens drei Sätzen über drei Zeilen.
    - Und eine volle A4-Seite ohne einzigen Absatz ist eher ungewöhnlich.
- **Kommasetzung** ist nicht fakultativ!!! Es hat sich in den letzen Jahrzehnten dazu einiges geändert, aber es gibt sie noch, die Kommas ... und sie retten weiterhin Leben ("Wir essen jetzt Kevin" und "Wir essen jetzt, Kevin")
- Übrigens nutzt man das Komma in deutsch auch als Dezimaltrennzeichen. Daher nicht einfach Dezimalzahlen mit Punkt aus anderen Programmen übernehmen. Der Punkt wäre in deutsch das Tausender-Trennzeichen.
- In der modernen technischen Welt verwenden wir häufig **englische Begriffe** für Anlagen, Verfahren, etc. Bitte ruhig mal im Duden nachschauen, ob es das jeweilige Wort so schon in die deutsche Sprache wie "Download" geschafft hat. Wenn nicht, sollte man schauen, ob man nicht auch ein deutsches Wort findet.
- Wissenschaftliche Arbeiten sollten in **unpersönlicher Schreibweise** verfasst werden. Auch wenn man immer wieder andere Beispiele findet, empfehle ich diese Form, um eine sachliche Darstellung zu unterstreichen.
- Überschriften werden immer in Großschreibung begonnen

    [Groß- und Klein­schrei­bung](https://www.duden.de/sprachwissen/rechtschreibregeln/Gro%C3%9F-%20und%20Kleinschreibung#D86)

### Struktur oder Gliederung
<a id='Struktur_Gliederung'></a>

Wissenschaftliche Arbeiten gliedern sich im Wesentlichen immer gleich:

- **1. Einleitung**
    - Die Einleitung dient der Einführung in das Thema und das Themengebiet. Es ist häufig viel zu kurz in studentischen Arbeiten verfasst.
    - Bilder/Diagramme zur Erläuterung sollen verwendet werden, ja sogar eine Zusammenfassung zum **Stand der Technik**, der dann die **Aufgabenstellung** motiviert, die selbst noch einmal kurz erläutert wird
    - häufig wird der Inhalt der Arbeit noch einmal kurz zusammengefasst - Was kommt in den nächsten Kapiteln?
    - Umfang von 2-4 Seiten durchaus erwünscht
- **2. Grundlagen**/Stand der Technik
    - Hier können noch mal die notwendigen grundlegenden Zusammenhänge des Themengebietes dargestellt werden. Formal gesehen ist das überflüssig, da es ja Stand der Technik ist und somit den Leser*innen zugänglich. Aber wenn man ehrlich ist, ist man nicht überall Experte und es ist hilfreich, wenn einem noch mal einige Dinge erläutert werden, die nicht in der allgemeinen Ingenieurausbildung in der Tiefe vorhanden sind.
    - beschränken Sie es auf das Notwendigste - einfaches Lehrbuchwissen ist meist fehl am Platz, Zusammenhänge aus der Spezialliteratur nicht
    - sollte nicht mehr als 20% des Umfangs der Arbeit ausmache
    - Referenzieren Sie sauber die Literatur!
- **3. Material und Methoden**
    - Den Lesern muss erklärt werden, wie man bestimmte Versuche/Experimente/Modelle aufgebaut und durchgeführt hat, damit man verstehen kann, was im Details gemacht wurde und worauf man achtet, wenn man es ebenso durchführen möchte
    - nochmal: es muss so erklärt werden, dass es ein anderer (Wissenschaftler/Ingenieur) ebenso aufbauen und durchführen kann! Wissenschaftliche Erkenntnis wird erst dann bestätigt, wenn sie wiederholbar ist. Daher in diesem Kapitel exakt arbeiten, ohne ins Geschwafel zu verfallen.
    - hier können auch Literaturreferenzen zu Methodiken und Geräten/Software verwendet werden
- **4. Ergebnisse**
    - Hier beginnt das Herzstück Ihrer Arbeit. Hier werden Ihre, allein Ihre Ergebnisse vorgestellt.
    - Hier wird nicht bewertet! ... Ja, ich weiß, jetzt denkt man, was schreibt man denn da? "Nicht Bewerten" heißt nicht "Nicht Beschreiben". Sie beschreiben die Ergebnisse, so dass der Leser durch diese von Ihnen geführt wird. Ein Diagramm beinhaltet sich alle wichtigen Erkenntnisse, aber nicht jeder wird diese sofort genauso erkennen wie Sie. Daher beschreiben Sie, was Sie in den Ergebnissen/Diagrammen sehen. Dabei können Sie auch Ausreißer oder Gründe für bestimmte Verläufe erklären. Aber Sie bewerten nicht, z.B. sie sagen hier noch nicht, ob die Ergebnisse auch zu den Erkenntnissen anderer Autoren passen (dies kommt in der Diskussion, nächstes Kapitel)
    - in diesem Kapitel keine Literaturreferenzen mehr - hier gibt es nur Ihre Ergebnisse!
    - man findet häufig in der Literatur, dass Autoren da Kapitel "Ergebnisse und Diskussion" nennen und auch so die Inhalte füllen. Dieses Vermischen klingt erst einmal logischer und ist auch einfacher zu schreiben (für Anfänger), aber es macht die Trennung zwischen Ihren Ergebnissen und der Bewertung dieser schwieriger, da dies unterschiedliche Ziele verfolgt.
- **5. Diskussion**
    - gehört ebenso zum Herzstück Ihrer Arbeit
    - Jetzt kommt die Bewertung Ihre Ergebnisse:
        - Vergleichen Sie diese zur Literatur (schön mit Referenzen arbeiten, wahrscheinlich einige aus der Einleitung den Grundlagen),
        - Wie passt das in die Theorie/Modellvorstellung zum Problem?
        - Welche Konsequenzen ergeben sich aus den Ergebnissen? Was kann man daraus schlussfolgern? Neue Modellansätze, etc.
    - Gliedern Sie diese Kapitel in weitere Überschriften, damit man die Themen klar erkennen kann. Dabei müssen Sie nicht genau der Beschreibung der Ergebnisse folgen, sondern können auch "quer" zu den Ergebnissen gliedern, so wie es am besten gelesen und verstanden werden kann.
    - Hier dürfen sie (auch) "spinnen". Teilen Sie Ihre Gedanken/Theorien dem Leser mit, damit dieser damit weiterarbeiten kann. Es muss wissenschaftlich sauber und nachvollziehbar sein, aber es darf auch mit Mut geschlussfolgert und in die Glaskugel interpretiert sein.
- **6. Zusammenfassung und Ausblick**
    - Die Überschrift sagt eigentlich schon alles: kurz das Problem, Vorgehen und Ergebnisse zusammenfassen und einen Ausblick geben
    - Der Ausblick ist ganz wichtig. Zeigen Sie auf, welche nächsten Schritte getan werden sollten/müssen. Wiederum, lassen die Leser an Ihren Gedanken zum Thema teilhaben
    - hier kommen keine Referenzen, Abbildungen oder ähnliches, nur Fließtext in Absätzen strukturiert
- **Literatur**
    - Das Literaturverzeichnis kommt am Ende der Arbeit und beinhaltet jegliche verwendete Referenz zur Literatur oder Stand der Technik, also Bücher, Artikel, Webseiten, etc.
    - Der Fokus liegt auf Referenzen, die den Lesern auch zugänglich sein können. Ausgedruckte Vorlesungsskripte, die es nicht online gibt, können für Ihr Verständnis sehr geholfen haben, sind aber als Referenz kaum nachvollziehbar
    (aber Ausnahmen bestätigen auch hier die Regel, nicht übertreiben)
    - Referenzen auf Webseiten sind ok, aber diese sollten nicht den überwiegenden Teil ausmachen. Auch wenn man vieles zu naturwissenschaftlichen Grundlagen oder den Ingenieurwissenschaften im Internet findet, ist die Quelle doch meist ein Buch.
    - sauber und vollständige Referenzen (man muss mit diesen Angaben auch die Quellen finden)

Die Überschriften können dabei dem Thema entsprechend auch anders lauten, aber inhaltlich sollte genau diese Struktur zu finden sein.

Achso, die Frage: Wie lang muss/darf die Arbeit sein? 
Es gibt eigentlich keine Seitenvorgabe. Schreiben Sie alles vollständig auf und fassen Sie sich so kurz und exakt wie möglich (kein Geschwafel). Je nachdem wie viel Sie am Thema gearbeitet und Ergebnisse erzeugt haben, wird sich passender ein Umfang einstellen. (mal als Hausnummer der Seitenzahlen aus der Erfahrung: oberer zweistelliger Bereich)

### Abbildungen
<a id='Abbildungen'></a>

Abbildungen sind gerade in ingenieurwissenschaftlichen Arbeiten essentiell, um Zusammenhänge oder auch Bauteile/Anlagen darstellen zu können. Weiterhin werden erfasste oder berechnete Daten in Diagrammen dargestellt. Dabei sind folgende Dinge zu beachten:

- **Bildgröße -** Ein Bild sollte nicht mehr als ein 1/3 der Höhe des Textfeldes einnehmen, wobei aber die gesamte Textbreite ausgenutzt werden kann, diese aber nicht überschritten werden sollte
- **Bildinhalt** - Ein Bild transportiert Informationen. Diese sind so zu strukturieren, dass die Leser diese möglichst einfach aufnehmen können. Also keine überladenen Diagramme (mit mehr als fünf Kurven), keine Anlagenfotos ohne Beschriftung der Baugruppen (Was sieht man da? Was ist wichtig zu erkennen?), keine Mikroskopaufnahmen ohne Beschriftung (ähnliche wie Anlagenfotos).
- **Bildbeschriftung** - Die Bildbeschriftung, unterhalb oder neben der Abbildung, sollte so umfangreich sein, dass diese allein mit dem Bild, außerhalb der Arbeit, lesbar und verständlich ist. Die Unterschrift kann dabei mehrere Zeilen oder sogar mehrere Sätze umfassen. Knapp aber vollständig bitte.
Referenzieren Sie die Quelle von Bildern, die nicht von Ihnen kommen (ggf. müsste auch die Freigabe des Rechteinhabers eingeholt werden)
- **Bildreferenz** - Jedes Bild hat eine Referenz im Text (z.B. "s. Abb. 10")! Noch mal anders: Es gibt kein Bild, welches nicht im Text erwähnt ist! D.h. es gibt kein "wie im *nachfolgenden* Bild ..." und es gibt auch keine Bilder ohne Bezug im Text.

Entsprechend einer konsistenten Darstellung von Skizzen oder Schemata in der Arbeit empfiehlt sich die eigene Anfertigung mit geeigneter Software. Dies kann durchaus auch künstlerische Fähigkeiten erfordern bzw. diese mit ein wenig Übung schulen.

- **Beispiel**

```{figure} Hinweise/Untitled_2.png 
--- 
width: 500px 
name: Untitled_2
--- 
Beispielabbildung mit zwei Abbildungen nebeneinander mit zugehöriger Bildbeschriftung  
``` 

```{figure} Hinweise/Untitled_3.png 
--- 
width: 500px 
name: Untitled_3
--- 
Beispielabbildung mit drei Abbildungen nebeneinander mit zugehöriger Bildbeschriftung  
``` 

```{figure} Hinweise/Untitled_4.png 
--- 
width: 500px 
name: Untitled_4
--- 
Beispielabbildung mit einer Abbildung mit zugehöriger Bildbeschriftung  
``` 

### Tabellen
<a id='Tabellen'></a>

Tabellen sind ähnlich wie Abbildungen zu betrachten und es treffen im Wesentlichen die gleichen Aussagen zu. Allerdings gibt es kleine Unterschiede bzw. Zusätzen:

- die Tabellenbeschriftung erfolgt nicht unter der Tabelle, sondern über dieser!
- Tabellen werden in der Referenz im Text nicht abgekürzt, also "s. Tabelle 12" und nicht "s. Tab. 12"
- die verwendete Schriftart in Tabellen sollte der Größe des allgemeinen Fließtextes entsprechen bzw. maximal 1-2 pt kleiner sein.

### Mathematische Formeln
<a id='MathematischeFormeln'></a>

In den Ingenieurwissenschaften geht es ohne mathematische Formeln nicht. Meist muss man in der Darstellung der Grundlagen schon ran und die wesentlichen Gleichungen einführen. Dazu folgende Bemerkungen:

- Optisch ansprechende Formeln und Gleichungen werden in LaTeX gesetzt. Selbst wenn man ein anderes Textverarbeitungsprogramm verwendet, könnt man die LaTeX-Formeln als Bild erzeugen und darin verwenden. Am besten ist natürlich, man schreibt gleich in LaTeX.
- Gleichungen werden leicht vom umgebenden Text abgesetzt zentriert dargestellt.
- Multiplikationszeichen werden häufig nicht extra dargestellt. Generell empfiehlt sich der Blick in die Literatur, wie andere Autoren in dem jeweiligen Bereich die Gleichungen darstellen.
- Alle verwendeten Variablen müssen im umgebenden Text bei erstmaliger Verwendung erklärt werden. Selbst wenn es ein Symbolverzeichnis für die Arbeit gibt, ist von dieser Regel nicht abzuweichen, damit der Lesefluss nicht gestört wird. Denken Sie an die Dramaturgie Ihrer Arbeit: In Buch und Film werden Charaktere auch beim ersten Erscheinen (indirekt) vorgestellt.
- Variablen sind eindeutig zu verwenden. Ein "a" kann z.B. nicht in der einen Gleichung ein Beschleunigung sein und in einer anderen eine Länge. Darauf ist besonders zu achten, wenn man Gleichungen aus verschiedenen Quellen verwendet.
- Gleichungen sollten generell nummeriert werden, wenn man sie später noch einmal referenzieren möchte. Die Gleichungsnummer wird dazu in geschweiften Klammern am rechten Rand des Textbereiches angegeben.
- Gleichungen werden, im Gegensatz zu Tabellen und Abbildungen, nur nachfolgend referenziert. D.h. es kann keine Referenz vor der ersten Darstellung der Gleichung geben, sondern nur nachfolgend, wenn man noch mal Bezug darauf nehmen möchte. Letztendlich ist eine Gleichung ja kein extra Objekt wie ein Abbildung, sondern sie wird wie Text gebildet, nur eben in der mathematischen Sprache.
- **Beispiel**

```{figure} Hinweise/Untitled_5.png 
--- 
width: 500px 
name: Untitled_5
--- 
Beispiel für die Verwendung von mathematischen Formeln 
``` 

### Literaturreferenzen
<a id='Literaturreferenzen'></a>

Zu Literaturquellen gehören Bücher, Dokumente, Webseiten aller Art. Wichtig ist dabei, dass die Leser diese Quellen auch einsehen können. Auch wenn dies nicht immer gelingt, sollte der Anspruch diesbezüglich hoch sein. Sicherlich müssen nicht alle allgemein bekannten Zusammenhänge mit Quelle belegt sein, z.B. sind die Energieerhaltungssätze sicher allgemein bekannt. Aber gerade die Aussagen zum Stand der Technik sollten sauber referenziert werden.

Selbst Gespräche könnten, wenn auch selten, als Quelle verwendet werden. Dies sollten dann aber tatsächlich Expertengespräche sein mit den Lesern bekannten Experten im Fachgebiet. Dies kann man nutzen, um den Zusammenhang der eigenen Aussagen noch einmal besser darzustellen. Man würde diese mit "private communication" referenzieren.

Wie referenziert man? In den Ingenieurwissenschaften hat sich eine numerischer Referenzierungstyp in eckigen Klammern etabliert (s. Beispiele). D.h. es wird jeder Quelle eine Nummer zugewiesen, die dann als Referenz verwendet werden kann. Dabei kann das Literaturverzeichnis in

- alphabetischer Reihenfolgen der Referenzen oder
- in der Reihenfolge des Erscheinen im Text

sortiert werden. Im ersten Fall ist das Literaturverzeichnis einfacher zu lesen, wenn man Autoren sucht. Allerdings beginnt dann die erste Referenz im Text nicht mit [1]. Genau andersherum sind Vor- und Nachteil bei der zweiten Variante zu verstehen. Verwendet man eingebundene Datenbanksysteme (wie bei LaTeX mit BibTeX möglich) kann dies aber jederzeit gewechselt und dann nach Geschmack entschieden werden.

Die Referenzen erfolgen direkt nach Nennung eines Autoren oder eines Bezuges (z.B. bei Normen) oder am Satzende, *vor dem Punkt (um den Fließtext und den nächsten Satz nicht zu stören)*, wenn sich die Referenz auf die Aussage im Satz bezieht. Bezieht sich die Literaturquelle oder die -quellen auf einen ganzen Absatz, werden diese nach dem letzten Satz, *hinter dem Punkt*, genannt. Dazu folgen hier Beispiele.

- **Beispiele**

```{figure} Hinweise/Untitled_6.png 
--- 
width: 500px 
name: Untitled_6
--- 
Beispiel für ein Literaturverzweis im Text 
``` 

```{figure} Hinweise/Untitled_7.png 
--- 
width: 500px 
name: Untitled_7
--- 
zugehörigeres Literaturverzeichnis 
``` 

---

**zu tun:**...
 
- Hinweise zur Darstellung des wissenschaftlichen Inhalts

    - In diesem Abschnitt geht es einige Hinweise zur Darstellung des Inhaltes der wissenschaftlichen Arbeit.

- Zeitmanagement

    - Doku soviel wie Ergebnisse

- Gute Diagramme erzeugen
 
    - fitten, excel smoothing, bild von xkcd
