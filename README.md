# LucesLed
Código para arreglar unas luces de navidad que salieron dañadas y con una raspberri PI3 la arreglé.
# Descripción del Código

Este código en Python utiliza la biblioteca RPi.GPIO para controlar los pines GPIO de una Raspberry Pi. Está diseñado para realizar una serie de patrones de parpadeo con dos LEDs conectados a los pines 7 y 11.

## Configuración Inicial

```python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
```
El bucle principal (while True:) se repite infinitamente, y después de cada secuencia de parpadeo, se apagan ambos LEDs antes de comenzar la siguiente secuencia. El programa continuará ejecutándose hasta que sea interrumpido manualmente.
```python
while True:
    GPIO.output(7, False)
    GPIO.output(11, False)

    timeout = time.time() + 60*1  # 1.5 minutos desde ahora
    while time.time() < timeout:
        intermitente()

    timeout = time.time() + 60*1.5  # 1.52 minutos desde ahora
    while time.time() < timeout:
        continuo()

    timeout = time.time() + 60  # 0.5 minutos desde ahora
    while time.time() < timeout:
        intermitenteRapido()
```
