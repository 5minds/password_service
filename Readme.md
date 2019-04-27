# Passwort Service

Projekt um einen Service zu erstellen, der einfach und vielseitig Passwörter
bereitstellen kann.

## Was sind die Ziele dieses Projekts?

Wir haben an vielen Stellen die Notwendigkeit Passwörter nach verschiedenen
mustern zu generieren.

Die hier vorgestellte Lösung verwendet das Perl Modul `Crypt::HSXKPasswd`.

Dieses ist ein Standard Werkzeug, es ist gut Dokumentiert, wird aktiv gepflegt
und kann als gut geeignet für diese Aufgabe angesehen werden.

Es unterstützt verschiedene Konfigurationen, um Passwörter zu generieren, die
einfach ausgetauscht werden können. So ist es möglich, für verschiedene
Szenarien einfache Regel zu hinterlegen, wie Passwörter zu generieren sind.

## Wie kann ich das Projekt aufsetzen?

### Voraussetzungen

**Production**

* Docker
* Perl (im Container)
* Python (im Container)

**Development**

Zusätzlich, zu den unter Production beschrieben Abhängigkeiten, wird folgendes
benötigt:

* Python 2.7
* virtualenv

### Setup Production

Die Software, wird in dem Docker-Container vollständig gebaut, das kann Zeit in
Anspruch nehmen. Es ist normal, dass der Build ca. eine viertel Stunde
benötigt.

`1.08s user 0.69s system 0% cpu 15:41.40 total`

Das Setup für Production, ist ein Docker-Container, er wird wie folgt gebaut.

```bash
$ docker build -t <name> .
$ docker run -it <name> /bin/bash

# und dann im Container:

root@2589325fc0e1:/# hsxkpasswd -p XKCD 10
continue-LAST-RATHER-HUMAN-READ
anything-single-CATTLE-fire-salt
SPEED-WELCOME-NORTHERN-PULLED-YOUNG
MISS-wind-miss-march-MOVEMENT
SOUTH-WRONG-FRESH-dark-HOLLAND
VOWEL-SUDDEN-EXCEPT-heavy-design
time-DIVIDED-mile-MOUNTAIN-INSTEAD
moon-BELGIUM-NEEDLE-FOOL-PAIR
baby-PROCESS-east-suppose-late
CAME-PROBABLY-pulled-shot-perfect
```

### Setup Development

1. Python virtualenv muss installiert sein

   ```bash
   pip install virtualenv
   ```

1. Einrichten der virtualenv

   ```bash
   virtualenv -p python2.7 .
   ```

1. Aktivierung der virtualenv

   ```bash
   source bin/activate
   ```

   Alles was wir nun installieren landet in den lokalen Ordnern und nicht im
   System Hauptverzeichnis. Die erfolgreiche Installation der virtualenv kann
   mit folgendem Verfahren getestet werden:

   ```python
   >>> import sys
   >>> sys.prefix
   '/Users/cmg/src/5minds/password_service/app/bin/..'
   ```

   Der angezeigte Pfad sollte im aktuellem Verzeichnis liegen.

1. Installieren der Abhängigkeiten

   Im app Verzeichnis befindet sich eine requirements.txt, diese enthält die
   Pakete, die der Service benötigt. Der folgende Aufruf installiert diese
   lokal.

   ```bash
   pip install -r requirements.txt
   ```

1. Anfügen zusätzlicher Abhängigkeiten

   Werden zusätzliche Abhängigkeiten benötigt, benutzt man folgenden Aufruf:

   ```bash
   pip install <packet>
   ```

1. Einfrieren von Abhängigkeiten

   ```bash
   pip freeze > requirements.txt
   ```

   Diese Abhängigkeiten sollten eingecheckt werden.

1. Deaktivierung der virtualenv

   ```bash
   deactivate
   ```
