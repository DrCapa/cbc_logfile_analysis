# Cbc logfile Analyse
Gegeben ist eine einfache Funktion zur Analyse und Visualisierung von Cbc logfiles. Die Funktion basiert auf dem klassischen Outputformat des Solvers der Version 2.9.7. 

Das Projekt enthält:
* analysis_cbc_logfile.py: beinhaltet die Analysefunktion,
* Ordner input: mit ausgewählten logfiles für Tests,
* example.py: ein einfaches Beispiel zur Verwendung der Funktion.

Gegenwärtig sind zwei Teilfunktionen enthalten:
1. Für alle logfiles im input Ordner wird eine Zusammenfassung für ausgewählte Merkmale erstellt. Es ist natürlich möglich die Merkmale zu erweitern oder zu modifizieren. Falls keine Zusammenfassung gewünscht ist, kann das optionale Argument **`summary=False`** gesetzt werden.
2. Zusätzlich ist es möglich eine Visualisierung des Konvergenzverhaltes für gefundene Teillösungen zu erstellen, solange mindestens 2 Teillösungen gefunden wurden. Diese Funktionalität kann mit dem optionalen Argument **`plot=True`** aktiviert werden

Die Funktion erzeugt den Ausgabeordner output für die Zusammenfassung im Excelformat und einen Unterordner für die Grafiken.