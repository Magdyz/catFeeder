import RPi.GPIO as GPIO
import time
import logging

#Logging data into a separate file called feeding.log

logging.basicConfig(filename='feeds.log', level=logging.DEBUG,
    format='%(asctime)s:%(message)s')

servoPin = 17
def move():
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin,50)
#feed number
feed = 3
p.start(2.5) 

try:
    for x in range(feed):
        x = move()
        logging.debug("One feed is done")
        time.sleep(0.5)

#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(10)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(5)
#    time.sleep(0.5)
#    p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
