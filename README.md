# aMAZEing-buggy


# Konfiguration
Empfohlen, aber nicht Notwendig ist ein frisch installiertes Raspbian auf ihrem Pi.
Anschließend sollten sie ihren Pi mittels<code>sudo apt-get update && sudo apt-get upgrade -y</code>(was einige minuten in anspruch nehmen kann) auf den aktuellsten stand bringen.

Nun können sie das Github Repo mithilfe von <code>git clone https://github.com/Arzeg/aMAZEing-buggy/</code> kopieren.
Außerdem verwende ich die Library rpi_ws281x von jgarff. Diese kopiere ich in das zuvor geklonte repo mit 

<code>cd ~/Desktop/aMAZEing-buggy</code>

<code>git clone https://github.com/jgarff/rpi_ws281x</code>

Bei mir liegt der Ordner im verzeichnis <code>~/Desktop</code> falls sie diesen dort nicht hinkopiert haben, müssen sie in dem bash Script den Pfad zum ausführen des LED Scripts anpassen. 

Das Script unterbodenbeleuchtung.py (welches sich nur leicht von dem strandtest.py) unterscheidet wird noch in den examples ordner der rpi_ws281x library geschoben.
<code>mv unterbodenbeleuchtung.py ~/Desktop/aMAZEing-buggy/rpi_ws281x/python/examples/</code>

Damit ihre LEDs auch beim Starten des Pi's direkt mit starten, müssen sie das Script in den autostart Ordner legen. Dafür gehen sie in das Verzeichnis wo sich das Script led_autostart.sh befindet und geben anschließend<code>sudo mv led_autostart.sh /etc/init.d/</code>ein.
