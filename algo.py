# Bibs einbinden
import random
import time


import RPi.GPIO as GPIO
from gpiozero import Robot

# from thread import start_new_thread

# Modus für GPIO Pins wählen

GPIO.setmode(GPIO.BCM)  # bestimmt den GPIO bin innerhalb des boards nicht die Kontaktpin nummer

# GPIO Pins zuweisen
GPIO_TRIGGER = 21
GPIO_ECHO_V = 22
GPIO_ECHO_L = 23
GPIO_ECHO_R = 19
GPIO_ECHO_H = 20
motor_L = (7, 8)
motor_R = (9, 10)

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


    temp_time = time.time()
    temp_time_start = temp_time

    # speichere zeiten
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
        temp_time = time.time()
#        print ("while 1: ", temp_time)
        if temp_time > (temp_time_start + .200): break
#        print ("while 1")

    temp_time = time.time()
    temp_time_start = temp_time

    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
        temp_time = time.time()
#        print ("while 2: ", temp_time)
        if temp_time > (temp_time_start + .200): break
  #      print ("while 2")

    # Calculate difference
    diff = stop_time - start_time

    # Multipliziere mit Schallgeschwindigkeit (34300 cm/s) & teile durch 2 da hin und zurück
    distance = (diff * 34300) / 2
    return distance

def fahr_los_righthand():
    car = Robot(motor_L, motor_R)
    abstand = 40
    abstand_vorne = 10
    abstand_fehlerwert = 1700
    while True:
        vorne = distance(GPIO_ECHO_V)
        rechts = distance(GPIO_ECHO_R)
        links = distance(GPIO_ECHO_L)
        hinten = distance(GPIO_ECHO_H)
        # solange rechts kein gang fahr gradeaus
        if rechts < abstand and vorne > abstand_vorne:
            car.forward(0.6)
            print ("vorwärts!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
        # Wenn gang rechts dann stop
        elif rechts > abstand:
            car.stop()
            time.sleep(0.1)
            print ("rechts versuch!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
            rechts=distance(GPIO_ECHO_R)
            # Erneute Prüfung von Abstand rechts
            if rechts > abstand and rechts < abstand_fehlerwert:
                if vorne > abstand_vorne:
                    car.forward(0.6)
                    time.sleep(0.37)
                car.right(0.6)
                print ("rechts!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
                time.sleep(1.25)  # drehe nach rechts
                car.forward(0.6)
                time.sleep(1.3)
        # wenn nur links gang fahre links
        elif rechts < abstand and vorne < abstand and links > abstand:
            car.stop()
            print ("links versuch!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
            time.sleep(0.1)
            links = distance(GPIO_ECHO_L)
            if links > abstand and links < abstand_fehlerwert:
                if vorne > abstand_vorne:
                    car.forward(0.6)
                    time.sleep(0.37)
                car.left(0.6)
                print ("links!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
                time.sleep(1.25)
                car.forward(0.6)
                time.sleep(1)
        # Sackgasse. wende auto
        elif hinten > abstand_vorne:
            car.stop()
            time.sleep(0.1)
            print ("wenden versuch!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
            vorne = distance(GPIO_ECHO_V)
            rechts = distance(GPIO_ECHO_R)
            links = distance(GPIO_ECHO_L)
            hinten = distance(GPIO_ECHO_H)
            if rechts < abstand and vorne < abstand and links < abstand and hinten > abstand_vorne:
                car.left(0.6)
                print ("wenden!\t vorne: ", vorne, "\t rechts :", rechts, "\t links: ", links, "\t hinten: ", hinten)
                time.sleep(1.1)

def ziellos():
    car = Robot(motor_L, motor_R)
    random.seed()
    richtungsliste = []
    links = 0
    vorne = 1
    rechts = 2
    hinten = 3
    abstand = 40
    abstand_vorne = 10
    abstand_fehlerwert = 1700
    while True:
        vorne_d = distance(GPIO_ECHO_V)
        rechts_d = distance(GPIO_ECHO_R)
        links_d = distance(GPIO_ECHO_L)
        hinten_d = distance(GPIO_ECHO_H)
        car.forward()   # fahre erstmal vorwärts
        #füge erlaubte richtungen basierend auf dem abstand zur liste hinzu
        if vorne_d > abstand_vorne:
            car.stop()
            vorne_d = distance(GPIO_ECHO_V)
            if vorne_d > abstand_vorne: richtungsliste.append(vorne)
        if links_d > abstand:
            car.stop()
            links_d = distance(GPIO_ECHO_L)
            if links_d > abstand and links_d < abstand_fehlerwert: richtungsliste.append(links)
        if rechts_d > abstand:
            car.stop()
            rechts_d = distance(GPIO_ECHO_R)
            if rechts_d > abstand and rechts_d < abstand_fehlerwert: richtungsliste.append(rechts)
        if not richtungsliste: richtungsliste.append(hinten)
        print (richtungsliste)
        richtung = random.choice(richtungsliste)
        richtungsliste.clear()
        # wähle richtung und reagiere dementsprechend
        if richtung == links:
            print ("links!\t vorne: ", vorne_d, "\t rechts :", rechts_d, "\t links: ", links_d, "\t hinten: ", hinten_d)
            if vorne > abstand_vorne:
                car.forward(0.6)
                time.sleep(0.45)
            car.left(0.77)
            time.sleep(1.25)
            car.forward(0.6)
            time.sleep(1)
        elif richtung == vorne: car.forward(0.6)
        elif richtung == rechts:
            print ("links!\t vorne: ", vorne_d, "\t rechts :", rechts_d, "\t links: ", links_d, "\t hinten: ", hinten_d)
            if vorne > abstand_vorne:
                car.forward(0.6)
                time.sleep(0.45)
            car.right(0.77)
            time.sleep(1.25)
            car.forward(0.6)
            time.sleep(1)
        elif richtung == hinten:
            print ("links!\t vorne: ", vorne_d, "\t rechts :", rechts_d, "\t links: ", links_d, "\t hinten: ", hinten_d)
            car.left(0.6)
            time.sleep(1)


#fahr_los_righthand()
ziellos()
