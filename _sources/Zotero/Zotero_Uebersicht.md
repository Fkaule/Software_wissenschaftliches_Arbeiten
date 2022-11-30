# Literaturverwaltung mit Zotero

Zotero ist eine plattformübergreifende Software zur Verwaltung von Literatur. Wir empfehlen den [Kurs der HTWK Bibliothek](https://bibliothek.htwk-leipzig.de/de/kurse-und-beratung/online-tutorials/online-zotero-kurs/).

## Literatur finden

Auf folgenden Seite kann Literatur gefunden werden:

1. [google scholar](https://scholar.google.com/) Google Suchdienst für wissenschaftliche Arbeiten
2. [ResearchGate](https://www.researchgate.net/search): soziale Plattform für Wwssenschaftlen Austausch
3. [BASE - Bielefeld Academic Search Engine](https://www.base-search.net/) Suchdienst der Uni Bielefeld
4. [ResearchRabbit](https://www.researchrabbit.ai) App zum finden von Verknüpfungen , auch mit Zotero koppelbar

## Verknüpfung Zotero & Overleaf

1. Im Overleaf `Neue Datei` anklicken (links oben)
2. Auswahl `From External URL`
3. Unter `URL` folgenden Link einfügen:

   3. `https://api.zotero.org/users/<userID>/collections/<collectionKey>/items?format=bibtex&limit=100`
   4. <userID> kann in [https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys) + `Your userID for use in API calls is XXXXXXX` 3. Damit dies funktioniert müsst ihr eure Bibliothek Öffentlich machen unter [https://www.zotero.org/settings/privacy](https://www.zotero.org/settings/privacy) den Haken unter `Publish entire library` machen. Falls ihr das nicht wollt müsst ihr ein API Key erzeugen und diesen mit key=`<APIKEY> in der Anfrage mit übergeben 3. Den `collectionKey`findet ihr in der URL wenn ihr auf eure Bibliothek klickt. Wenn ihr einfach eure ganze Bibliothek wollt nutzt einfach den Link ohne`collections/<collectionKey>`(Der API Zugriff laesst aber nur 100 Eintraege zu, daher ist es manchmal sinnvoll nur eine Kollektion auszuwählen) `
   5. [Zotero Hilfe dazu](https://www.zotero.org/support/dev/web_api/v3/basics)

4. Unter `File Name` den Namen der Bibliothek abspeichern z.B. `my_zotero_bib`
