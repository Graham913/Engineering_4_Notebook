#type:ignore
import digitalio
import board
import time

led1 = digitalio.DigitalInOut(board.GP15)
led2 = digitalio.DigitalInOut(board.GP18)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
for x in range(10, -1,-1):
  if x == 0:
    print("liftoff!")
    led1.value = True
    time.sleep(.2)
    led1.value = False
    time.sleep(.2)
  else:
    print(x)
    time.sleep(.2)
    led2.value = True
    time.sleep(.2)
    led2.value = False
    time.sleep(.2)

while True:
  pass
