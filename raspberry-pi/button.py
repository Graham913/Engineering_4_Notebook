#type:ignore
import digitalio
import board
import time

led1 = digitalio.DigitalInOut(board.GP13)
led2 = digitalio.DigitalInOut(board.GP18)
button = digitalio.DigitalInOut(board.GP16) # double check if button is in right pin

led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT # put these defines after the LED defines and make sure you know if its PULL.DOWN 
button.pull = digitalio.Pull.DOWN

while True:
  if button.value == True: # make sure this encompasses the entire if else and the for x in range
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