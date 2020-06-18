import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Led_Azul = 23
Led_Vermelho = 16

GPIO.setup(Led_Azul,GPIO.OUT)
GPIO.setup(Led_Vermelho,GPIO.OUT)

try:
    while True:
        print("LED AZUL")
        GPIO.output(Led_Azul,True)
        GPIO.output(Led_Vermelho,False)
        time.sleep(2)
        print("LED VERMELHO")
        GPIO.output(Led_Azul,False)
        GPIO.output(Led_Vermelho,True)
        time.sleep(2)
        print("LED AZUL E VERMELHO LIGADOS")
        GPIO.output(Led_Azul,True)
        GPIO.output(Led_Vermelho,True)
        time.sleep(2)
        print("LED AZUL E VERMELHO DESLIGADOS")
        GPIO.output(Led_Azul,False)
        GPIO.output(Led_Vermelho,False)
        time.sleep(2)
except KeyboardInterrupt:
        print("DESLIGANDO...")
        GPIO.cleanup()