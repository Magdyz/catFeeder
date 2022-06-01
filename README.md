# catFeeder

This was my first project based on Python. 

It's automates a cat feeder to feed my cats at certain times every day. It is based on Rasberry pi any model that connects to the internet. 

## What you need!

- A servo
- Any 3D printed tower (I saw people using Pringles box)
- A circular plastic cover attached servo with holes to let the cat buscits out when the servo moves. I have used a plastic big yogurt cover with holes in it.

## The code 

Firstly, import the resourses needed which are `RPi.GPIO` which is for the ports that are connected to the physical Pi. Then `time` module, which is responsible for intervals between servo movements. The `logging` module is just to keep track of everytime the code runs.

```
import RPi.GPIO as GPIO
import time
import logging
```
The logging part could be removed for simplicity. After all, it doesn't guarantee that the servo worked, it only addes logs when the code runs. It saves to a file `feeds.log` in the same folder.

```
logging.basicConfig(filename='feeds.log', level=logging.DEBUG,
    format='%(asctime)s:%(message)s')
```
## Adjusting servo movements

I won't go into attaching servo pins and adjusting the movements because all of these depend on your Pi and Servo. Just make sure to check the manual for the servo and leave seconds between each movement in order not to get the servo going crazy. I have found the `time.sleep(0.5)` is enough rest for the servo to move smoothly.


```
servoPin = 17
def move():
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
```

This is the main skelton for any future upgrades. You could add a function to check current time and update the movement accordingly at certain times. 
You could also connect a button and get the `move()` function to run when the button is pressed. 

I have attached a video for elaboration. 

Good luck,
