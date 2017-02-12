import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#BUTTON SETUP
button = 19
GPIO.setup(button, GPIO.IN, pull_up+down=GPIO.PUD_UP)

#LED SETUP
led = 21
GPIO.setup(led, GPIO.OUT)
#Switch on

while True:
  input_state = GPIO.input(button)
  if input_state == False:
    print('Button Pressed')
    time.sleep(0.2)
    # Switch on LED
    GPIO.output(led, 1)
  else:

