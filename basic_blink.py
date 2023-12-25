from machine import Pin
import time
import neopixel

led = neopixel.NeoPixel(Pin(16),1)#crée un objet led

def blink():
    while True :
        led[0] = (0,0,255) #(r,g,b) ici bleu pur
        led.write() #met à jour l'état de la led
        time.sleep_ms(100)
        led[0] = (0,0,0)
        led.write()
        time.sleep_ms(100)

blink()