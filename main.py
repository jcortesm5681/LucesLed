## ESTE ARCHIVO FUE USADO EN LA RASPBERRY PICO
from machine import Pin
import time
led  =  Pin(14,  Pin.OUT)
led2 =  Pin(15,  Pin.OUT)
led3  =  Pin(25,  Pin.OUT)

def intermitenteR(): 
    #print('Intermitente!')
    led.value(1)
    led2.value(0)
    led3.toggle()
    time.sleep(0.1)
    led.value(0)
    led2.value(1)
    led3.toggle()
    time.sleep(0.1)
    led.value(1)
    led2.value(0)
    led3.toggle()


def intermitente(): 
    #print('Intermitente!')
    led.value(1)
    led2.value(0)
    led3.toggle()
    time.sleep(1.5)
    led.value(0)
    led2.value(1)
    led3.toggle()
    time.sleep(1.5)
    led.value(1)
    led2.value(0)
    led3.toggle()
    
    
def continuo(): 
    #print('Intermitente!')
    led.value(1)
    led2.value(0)
    led3.toggle()
    time.sleep(0.001)
    led.value(0)
    led2.value(1)
    led3.toggle()
    time.sleep(0.001)
    led.value(1)
    led2.value(0)
    led3.toggle()  
    




while True:
    led.value(0)
    led2.value(0)
    timeout = time.time() + 60 # 1 minutes from now
    while time.time() < timeout:
        #print("Interm")
        intermitente()
        
    timeout = time.time() + 60*1.5 # 1.5 minutes from now
    while time.time() < timeout:
        #print("Interm")
        continuo()
        
    timeout = time.time() + 60 # 1 minutes from now
    while time.time() < timeout:
        #print("Interm")
        intermitenteR()



    
