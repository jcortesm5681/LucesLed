import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
n=0;
def greet():
	print('Hello World!')



def intermitenteRapido(): 
	#print('Intermitente!')
	GPIO.output(7, True)
	GPIO.output(11,False)
	time.sleep(0.1)
	GPIO.output(7, False)
	GPIO.output(11,True)
	time.sleep(0.1)
	GPIO.output(7, False)
	GPIO.output(11,False)

def intermitente():
	#print('Intermitente!')
	GPIO.output(7, True)
	GPIO.output(11,False)
	time.sleep(1.5)
	GPIO.output(7, False)
	GPIO.output(11,True)
	time.sleep(1.5)
	GPIO.output(7, False)
	GPIO.output(11,False)


def continuo():
	#print('Continuo!')
	GPIO.output(7, True)
	GPIO.output(11,False)
	time.sleep(0.001)
	GPIO.output(7, False)
	GPIO.output(11,True)
	time.sleep(0.001)
	GPIO.output(7, False)
	GPIO.output(11,False)


while True:
	GPIO.output(7, False)
	GPIO.output(11,False)
	timeout = time.time() + 60*1	 # 1.5 minutes from now
	while time.time() < timeout:
		#print("Interm")
		intermitente()

	timeout = time.time() + 60*1.5 	 # 1.52 minutes from now
	while time.time() < timeout:
		#print(n)
		continuo()

	timeout = time.time() + 60	 # 0.5 minutes from now
	while time.time() < timeout:
		#print(n)
		intermitenteRapido()
