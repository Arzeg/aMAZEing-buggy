# aMAZEing-buggy


# Konfiguration
Empfohlen, aber nicht Notwendig ist ein frisch installiertes Raspbian auf ihrem Pi.
Anschließend sollten sie ihren Pi mittels<code>sudo apt-get update && sudo apt-get upgrade -y</code>(was einige minuten in anspruch nehmen kann) auf den aktuellsten stand bringen.

Nun können sie das Github Repo mithilfe von <code>git clone https://github.com/Arzeg/aMAZEing-buggy/</code> kopieren.
Bei mir liegt der Ordner im verzeichnis <code>~/Desktop</code> falls sie diesen dort nicht hinkopiert haben, müssen sie in dem bash Script den Pfad zum ausführen des LED Scripts anpassen. 

Damit ihre LEDs auch beim Starten des Pi's direkt mit starten, müssen sie das script in den autostart Ordner legen. Dafür gehen sie in das verzeichnis wo sich das Script befindet und geben anschließend<code>sudo mv led_autostart.sh /etc/init.d/</code>ein.

Wichtige Info NICHT LÖSCHEN!:

Pfad zum eigentlichen LED script ~/rpi_ws281x/python/examples/unterbodenbeleuchtung.py
