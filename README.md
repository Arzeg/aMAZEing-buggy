# aMAZEing-buggy        (IN BEARBEITUNG)
Der aMAZEing-buggy ist ein selbstgebautes Auto (mit unterbodenbeleuchtung!) welches mittels Ultraschallsensoren durch ein Labyrinth fährt.

# Konfiguration
Empfohlen, aber nicht Notwendig ist ein frisch installiertes Raspbian auf ihrem Pi.
In dem Projekt wurde die minimale desktop variante von der version Buster verwendet. Wenn sie ihren Pi an einen Bildschirm sowie Maus und Tastatur Angeschlossen haben, starten sie ihn. Sobald sie den desktop sehen, erscheint ein Wilkommens Fenster, wo sie den anweisungen folgen.
Nachdem ihr Pi neugestartet hat, gehen sie unter Start -> Einstellungen -> RaspberryPi Konfiguration -> Schnittstellen
dort setzen sie den Punkt für SSH auf Aktiviert. Wenn die IP-Adresse des Pi bekannt ist können sie sich nun Per Fernzugriff in den Pi einloggen. 
Anschließend sollten sie ihren Pi mittels<code>sudo apt-get update && sudo apt-get upgrade -y</code>(was einige minuten in anspruch nehmen kann) auf den aktuellsten stand bringen.

Nun können sie das Github Repo mithilfe von <code>git clone https://github.com/Arzeg/aMAZEing-buggy/</code> kopieren.
Außerdem verwende ich die Library rpi_ws281x von jgarff. Diese kopiere ich in das zuvor geklonte repo mit 

<code>cd ~/Desktop/aMAZEing-buggy</code>

<code>git clone https://github.com/jgarff/rpi_ws281x</code>

Bei mir liegt der Ordner im verzeichnis <code>~/Desktop</code> falls sie diesen dort nicht hinkopiert haben, müssen sie in dem bash Script den Pfad zum ausführen des LED Scripts anpassen. 

Das Script unterbodenbeleuchtung.py (welches sich nur leicht von dem strandtest.py) unterscheidet wird noch in den examples ordner der rpi_ws281x library geschoben.
<code>mv unterbodenbeleuchtung.py ~/Desktop/aMAZEing-buggy/rpi_ws281x/python/examples/</code>

Damit ihre LEDs auch beim Starten des Pi's direkt mit starten, müssen sie das Script in den autostart Ordner legen. Dafür gehen sie in das Verzeichnis wo sich das Script led_autostart.sh befindet und geben anschließend<code>sudo mv led_autostart.sh /etc/init.d/</code>ein.
Außerdem muss das bash script ausführbar gemacht und als default wert beim starten gesetzt werden.

<code>sudo chmod 755 /etc/init.d/led_autostart.sh</code>

<code>sudo update-rc.d led_autostart.sh defaults</code>

Nun installieren wir die benötigten Pakete
<code>sudo apt-get install gcc make build-essential python-dev git scons swig</code>

Die Audioausgabe muss deaktiviert werden, dafür muss folgende Datei bearbeitet werden
<code>sudo nano /etc/modprobe.d/snd-blacklist.conf</code>

Es wird folgende Zeile hinzugefügt
<code>blacklist snd_bcm2835</code>
Die Datei wird mit STRG+O gespeicher und mit STRG+X geschlossen

Außerdem müssen wir die Konfigurationsdatei bearbeiten
<code>sudo nano /boot/config.txt</code>

weiter unten befindet sich die folgende Zeile:
<code># Enable audio (loads snd_bcm2835)
dtparam=audio=on</code>

hier muss die untere zeile mit # auskommentiert werden

Dann Starten wir den Pi neu
<code>sudo reboot</code>


In diesem Verzeichnis sind nun einerseits einige C Dateien enthalten, welche einfach kompiliert werden können. Damit wir diese in Python verwenden können, müssen wir sie kompilieren:
<code>

cd ~/Desktop/aMAZEing-buggy/rpi_ws281x/

sudo scons

</code>



Nun führen wir die Installation durch
<code>

cd ~/Desktop/aMAZEing-buggy/rpi_ws281x/python/

sudo python setup.py build

sudo python setup.py install

</code>

<code>sudo update-rc.d led_autostart.sh defaults</code>

Nun müssen wir den dienst noch automatisch starten sobal der Pi hochgefahren ist, dazu ändern wir folgende datei

<code>sudo nano /etc/rc.local</code>

und fügen vor dem exit 0 noch folgendes ein:

<code>/etc/init.d/led_autostart.sh start</code>     // noch ändern zu /usr/local/bin/script.sh
