#! /bin/sh
#Switch case fuer den ersten Parameter

case "$1" in
    start)
 #Aktion wenn start uebergeben wird
        sudo PYTHONPATH=".:/home/pi/Desktop/aMAZEing-buggy/rpi_ws281x/python/build/lib.linux-armv7l-2.7" python /home/pi/Desktop/aMAZEing-buggy/rpi_ws281x/python/examples/unterbodenbeleuchtung.py -c
        ;;
    stop)
 #Aktion wenn stop uebergeben wird
        echo "Stoppe MeinProgramm"
        ;;
    restart)
 #Aktion wenn restart uebergeben wird
        echo "Restarte MeinProgramm"
        ;;
 *)
 #Standard Aktion wenn start|stop|restart nicht passen
 echo "(start|stop|restart)"
 ;;
esac
exit 0
