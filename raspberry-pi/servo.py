#type:ignore
import digitalio
import board
import time
import pwmio

from adafruit_motor import servo # make sure to have to correct imports in your adafruit library


led1 = digitalio.DigitalInOut(board.GP13)
led2 = digitalio.DigitalInOut(board.GP18)
button = digitalio.DigitalInOut(board.GP16)
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) # check the defines that this is in there

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
  if button.value == True:
    print("button")
    for x in range(10, -1,-1):
     if x == 0:
      print("liftoff!")
      led1.value = True
      time.sleep(.5)
      led1.value = False
      time.sleep(.5)
      servo1.angle = 0
     else:
      print(x)
      time.sleep(.5)
      led2.value = True
      time.sleep(.5)
      led2.value = False
      time.sleep(.5)

#while True:
#  pass