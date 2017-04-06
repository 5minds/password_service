# Passwort Service

Projekt und einen Image zu erstellen, das einfach und vielseitig Passwörter
bereitstellt.

## Was sind die Ziele dieses Projekts?

Wir haben an vielen Stellen die Notwendigkeit Passwörter nach verschiedenen
Schemata zu generieren. Das kann zu einer Unübersichtlichkeit führen.

Die hier vorgestellte Lösung verwendet das Perl Modul Crypt::HSXKPasswd.
Dieses ist ein Standard Werkzeug, ausgezeichnet Dokumentiert und gepflegt.

Es unterstützt verschiedene Konfigurationen, die einfach ausgetauscht werden können.

## Wie kann ich das Projekt aufsetzen?

### Voraussetzungen

**Production**

* Docker
* Perl (im Container)
* Python (im Container)

**Development**

Zusätzlich zu den Production beschrieben Abhängigkeiten wird folgendes benötigt:

* Python 2.7
* virtualenv

### Setup

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
