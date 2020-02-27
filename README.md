# aMAZEing-buggy        (IN BEARBEITUNG)
Der aMAZEing-buggy ist ein selbstgebautes Auto (mit unterbodenbeleuchtung!) welches mittels Ultraschallsensoren durch ein Labyrinth fährt.

## Konfiguration
Empfohlen, aber nicht Notwendig ist ein frisch installiertes Raspbian auf ihrem Pi.
In dem Projekt wurde die minimale desktop variante von der version Buster verwendet. Wenn sie ihren Pi an einen Bildschirm sowie Maus und Tastatur Angeschlossen haben, starten sie ihn. Sobald sie den Desktop sehen, erscheint ein Fenster, wo sie den konfigurationsanweisungen folgen.
Nachdem ihr Pi neugestartet hat, gehen sie unter Start -> Einstellungen -> RaspberryPi Konfiguration -> Schnittstellen
dort setzen sie den Punkt für SSH auf Aktiviert. Wenn die IP-Adresse des Pi bekannt ist können sie sich nun Per Fernzugriff in den Pi einloggen. 
Anschließend sollten sie ihren Pi mittels<code>sudo apt-get update && sudo apt-get upgrade -y</code>(was einige minuten in anspruch nehmen kann) auf den aktuellsten stand bringen.

Nun können sie das Github Repo mithilfe von <code>git clone https://github.com/Arzeg/aMAZEing-buggy/</code> kopieren.
Außerdem verwende ich die Library rpi_ws281x von jgarff. Diese kopiere ich in das zuvor geklonte repo mit 

```bash
cd ~/Desktop/aMAZEing-buggy
git clone https://github.com/jgarff/rpi_ws281x
```

Bei mir liegt der Ordner im verzeichnis <code>~/Desktop</code> falls sie diesen dort nicht hinkopiert haben, müssen sie in dem bash Script den Pfad zum ausführen des LED Scripts anpassen. 

Das Script <code>unterbodenbeleuchtung.py</code> (welches sich nur leicht von dem strandtest.py) unterscheidet wird noch in den examples ordner der rpi_ws281x library geschoben.
<code>mv unterbodenbeleuchtung.py ~/Desktop/aMAZEing-buggy/rpi_ws281x/python/examples/</code>

Damit ihre LEDs auch beim Starten des Pi's direkt mit starten, müssen sie das folgendes tun:

(Wichtig ist das in der rc.local datei, der Befehl vor <code>exit 0</code> eingefügt wird)
```bash
sudo chmod 755 /usr/local/bin/led_autostart.sh
sudo mv led_autostart.sh /usr/local/bin/
sudo nano /etc/rc.local
/usr/local/bin/led_autostart.sh start
```


Nun installieren wir die benötigten Pakete:

<code>sudo apt-get install gcc make build-essential python-dev git scons swig</code>

Die Audioausgabe muss deaktiviert werden, dafür muss folgende Datei bearbeitet oder falls nicht vorhanden erstellt und die entsprechende zeile eingefügt werden:
```bash
sudo nano /etc/modprobe.d/snd-blacklist.conf
blacklist snd_bcm2835
```

Außerdem müssen wir die Konfigurationsdatei mit <code>sudo nano /boot/config.txt</code>bearbeiten und die zeile <code>dtparam=audio=on</code> mit # auskommentieren. Hier ein ausschnitt aus der datei:
```bash
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```

Dann Starten wir den Pi neu
<code>sudo reboot</code>

In diesem Verzeichnis sind nun einerseits einige C Dateien enthalten, welche einfach kompiliert werden können. Damit wir diese in Python verwenden können, müssen wir sie kompilieren:

```bash
cd ~/Desktop/aMAZEing-buggy/rpi_ws281x/
sudo scons
```

Nun führen wir die Installation durch
```bash

cd ~/Desktop/aMAZEing-buggy/rpi_ws281x/python/

sudo python setup.py build

sudo python setup.py install
```
