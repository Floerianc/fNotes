


> Written with [StackEdit](https://stackedit.io/)

## **fNotes benutzen**

### -1. Inhalt
- **0.** Neue Notizen erstellen
- **1.** Notizen auswählen
- **1.1** Notizen öffnen
- **2.** Den Namen der Notiz ändern
- **3.** Deine Notiz schreiben
- **3.1** Einfach
- **3.2** Erweitert
- **4.** Notizen speichern
- **4.1** Automatisches Speichern (Tmp)
- **5.** Notizen löschen
- **6.** Mathematik
- **7.** Über
- **8.** Einstellungen


### 0. Neue Notizen erstellen
Klicke zuerst auf den **Note**-Knopf, welcher sich oben-links in dem Fenster befindet, danach klickt man auf **New**, um eine neue Notiz zu erstellen. Beachte dabei, dass jegliche Veränderung in der momentanen Notiz NICHT gespeichert wird, wenn man eine neue Notiz erstellt.

### 1. Notizen auswählen
Wenn man fNotes zum ersten Mal startet, bemerkt man eventuell Text, welcher sich in den zwei Kasten (obere Hälfte des Fensters) befindet. In dem Quellcode werden diese als "listWidget" und "tmpListWidget" bezeichnet

Wie man eventuell an dem Namen erkennen kann, handelt es sich hierbei um Listen, die mehrere Einträge/Artikel bzw. Notizen beinhalten können. Wenn man auf den Namen von einer Notiz klickt, wird der Inhalt der Notiz in den Editor (Die große Box in der unteren Hälfte des Fensters) gesetzt und der Name von der Notiz wird in das name-Label gesetzt.


#### 1.1 Notizen öffnen
Wenn ein Kollege, Freund oder ziemlich irgendjemand eine fNotes-Datei verschickt und man sie einsehen möchte, müssen sie auf **Note** (oben-links im Fenster) und dann auf **Open** klicken. Beachte dabei, dass jegliche Veränderung in der momentanen Notiz NICHT gespeichert wird. 

### 2. Den Namen der Notiz ändern
Um den Namen der Notiz zu ändern, müssen sie den Text in der nameLabel-Zeile verändern.

### 3. Deine Notiz schreiben
Diese Version von fNotes hat ein paar Funktionen, um deine Notiz zu bearbeiten.

### 3.1 Einfach:
- **F** >> Macht den markierten Text fett
- **U** >> Unterstreicht den markierten Text
- **K** >> Macht den markierten Text kursiv
- **L** >> Macht den markierten Text links-bündig
- **M** >> Zentriert den markierten Text
- **R** >> Macht den markierten Text rechts-bündig
- *SpinBox* (?px) >> Verändert die Größe vom markierten Text
- **Σ** >> Kann eine mathematische Aufgabe lösen
- *Die schwarzen Kasten* >> Verändert die Farbe vom markierten Text oder setzt den Marker ein, um die Hintergrundfarbe vom Text zu verändern.
- **•**  >> Erstellt eine Liste
- **1.** >> Erstellt eine Liste mit Zahlen
- **a.** >> Erstellt eine Liste mit dem Alphabet
- **IV.** >> Erstellt eine Liste mit den römischen Zahlen
- **Bild** >> Setzt ein Bild in den Editor rein
- **Tabelle** >> Erstellt eine Tabelle im Editor

### 3.2 Erweitert:
- **Gewicht der Schrift** >> Verändert die Gewicht der Schrift
- **Schrift** >> Verändert die Schriftart

### 4. Notiz speichern
Um eine Notiz zu speichern, klickt man auf **Note**, oben-links im Fenster, und dann auf **Save**. Dies speichert die Datei automatisch, damit man sie beim nächsten Mal, wenn sie das Programm öffnen, direkt wieder finden kann.

#### 4.1 Automatisches speichern (Tmp)
Dieses Programm speichert automatisch jegliche Notiz, die sie gerade bearbeiten. Diese Notizen kann man in dem tmpListWidget (der rechte Kasten in der oberen Hälfte des Bildschirms) einsehen. Diese Dateien enden immer mit dem Schlüssel "Tmp", damit man weiß, dass es sich hierbei um eine automatische Sicherung handelt. Wenn man nicht mit Tmp-Notizen bombadiert werden möchte, kann man sie auch löschen (Siehe 5.)

### 5. Notizen löschen
Eine Notiz kann man löschen, indem man auf den "Delete current note"-Knopf, unten-links im Fenster, drückt. Alternativ kann man eine Notiz löschen, indem man auf **Note** und dann auf **Delete** klickt.

### 6. Mathematik
Der einfache Rechner ( **Σ** ) kann simple mathematische Aufgaben lösen.
Dieser Rechner kann folgendes:
- Addition, Subtraktion, Multiplikation, Division und Modulo
- Quadratwurzeln | Verwendung: "sqrt(2)" -> 1.414...
- Sinus | Verwendung: "sin(2)" -> [Nummer]
- Kosinus | Verwendung: "cos(2)" -> [Nummer]
- Logarithmus | Verwendung: "log(2)" -> [Nummer]
- Exponentialfunktion | Verwendung: "exp(2)" -> [Nummer]
- Exponent	 | Verwendung: "pow(2, 3)" -> 8
	- Alternativ: 2 ^ 3 -> 8 **oder** 2 ** 3 -> 8
- Pi | Verwendung: "pi" -> 3.141...

### 7. Über
Um das "Über" Fenster zu öffnen: **Help** >> **About**.

### 8. Einstellungen
In dem Einstellungsmenü (**Weitere** >> **Einstellungen**) kann man ein paar Variablen bzw. Werte nach ihren Präferenzen einstellen.
Alle Einstellungen:
- Die Sprache der **Über**-Seite verändern (entweder Deutsch oder Englisch)
- Die Nachkommastellen im Rechner einstellen (zwischen 1 und 9, wenn man dort z.B. 5 einstellt, wird bei `1 / 3` die Zahl 0.33333 rauskommen)
- Das Interval für das automatische Speichern verändern (zwischen 0 und 300 Sekunden. Falls man 0 Sekunden eingibt, wird das automatische Speichern "komplett" ausgestellt. Im Quellcode wird die Wartezeit einfach auf 9,509,509 Sekunden gesetzt)
- Standard Schriftgroße setzen (zwischen 1px und 128px)
- Automatischer Zeilensprung ein- bzw. ausstellen.
