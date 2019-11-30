# BZraetsel
## BZraetsel 3
Als ertes denken wir uns eine Darstellung aus. Wir gehen von der Mitte aus nach außen und dann einen im Uhrzeigersinn. Das ganze sechs mal.
also:


6|6|6|6|6|6
14|x|x|x|x|x
4|x|x|x|x|x
x|x|x|x|x|x


die erste Spalte ist nur 6 also lassen wir sie weg


14|x|x|x|x|x
4|x|x|x|x|x
x|x|x|x|x|x


daraus ergeben sich die Bedingungen:
-Spaltenweise müssen sich die ersten beiden Zeilen auf 18 addieren
-Spaltenweise müssen sich die letzten beiden Zeilen und die mittlere Zeile der nächsten Spalte auf 24 addieren
(letzte Spalte mit erster Spalte ergänzen)

die oberen Zeilen können nur diese Paare sein:


1|17
2|16
3|15
4|14x
5|13
6|12x
7|11
8|10


d.h. es muss jede Kombination der Paare ausprobiert werden:
5 aus 6 auswählen sind 6 Möglichkeiten
5 anordnen sind 5! Möglichkeiten
diese 5 Paare können zeilenweise vertauscht sein => 2^5 Möglichkeiten
6*5!*2^5=23040
Die übrigen Felder können nun berechnet werden. Wenn der errechnete Wert groesser 0 und kleiner 20 ist und keine zahl ist die schon verwendet wird wurde die Lösung gefunden.
Das Ergebnis:
[

[14, 17, 7, 15, 5, 16],

[4, 1, 11, 3, 13, 2],

[19, 12, 10, 8, 9, 18]

]


[

[14, 16, 15, 5, 17, 7],

[4, 2, 3, 13, 1, 11],

[18, 19, 8, 10, 12, 9]

]


[
[14, 16, 5, 15, 7, 17],

[4, 2, 13, 3, 11, 1],

[18, 9, 8, 10, 12, 19]

]


[
[14, 7, 17, 5, 15, 16],

[4, 11, 1, 13, 3, 2],

[9, 12, 10, 8, 19, 18]

]

Theoretisch sind es nur zwei Lösungen, zwei sind jeweils San der 6-14-4 Achse gespiegelt. Die 4 liegt entweder zwischen 19 und 18 oder 9 und 18.
