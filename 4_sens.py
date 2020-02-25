# Bibs einbinden
import RPi.GPIO as GPIO
import time

from gpiozero import Robot

# Modus für GPIO Pins wählen
GPIO.setmode(GPIO.BCM) #bestimmt den GPIO bin innerhalb des boards nicht die Kontaktpin nummer

# GPIO Pins zuweisen
GPIO_TRIGGER = 21
GPIO_ECHO_V = 17
GPIO_ECHO_L = 18
GPIO_ECHO_R = 19
GPIO_ECHO_H = 20

# Richtung von GPIO Pins festlegen
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO_V, GPIO.IN)
GPIO.setup(GPIO_ECHO_L, GPIO.IN)
GPIO.setup(GPIO_ECHO_R, GPIO.IN)
GPIO.setup(GPIO_ECHO_H, GPIO.IN)

def distance(GPIO_ECHO):
        # Trigger Kalibrieren
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        # Zeiten
        start_time = time.time()
        stop_time = time.time()

        # speichere zeiten
        while GPIO.input(GPIO_ECHO) == 0:
                start_time = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
                stop_time = time.time()

        # Calculate difference
        diff = stop_time - start_time

        # Multipliziere mit Schallgeschwindigkeit (34300 cm/s) & teile durch 2 da hin und zurück
        distance = (diff * 34300) / 2
        return distance

try:
        while True:
                abstand_V, abstand_L, abstand_R, abstand_H = distance(GPIO_ECHO_V), distance(GPIO_ECHO_L), distance(GPIO_ECHO_R), distance(GPIO_ECHO_H)
                print ("Nach vorne: %.1f cm" % abstand_V + "\t Nach Hinten: %.1f cm" % abstand_H)
                print ("Nach Links: %.1f cm" % abstand_L + "\t Nach Rechts: %.1f cm" % abstand_R)
                print ()
                time.sleep(0.1)


except KeyboardInterrupt:
        print("Messung gestoppt")
        GPIO.cleanup()
