import RPi.GPIO as GPIO
import MAX6675.MAX6675 as MAX6675
import time
from pygame import mixer
CSK = 25
CS = 24
DO = 18
LED = 14
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

sensor = MAX6675.MAX6675(CSK,CS,DO)
mixer.init()
sound = mixer.Sound('Sirene.wav')
try:
    while True:
        Temp = sensor.readTempC()
        print("Temperatura ==> {0:0.2F}".format(Temp))
        if Temp > 40:
            GPIO.output(LED,True)
            sound.play()
        else:
            GPIO.output(LED,False)
            sound.stop()
        time.sleep(2)


except KeyboardInterrupt:
        print("\nFinalizado...")
        GPIO.cleanup()
