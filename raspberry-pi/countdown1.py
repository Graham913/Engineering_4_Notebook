#type:ignore
import digitalio
import board
import time

for x in range(10, -1,-1):
  if x == 0: #remember to use two equal signs in this instancce
    print("liftoff!")

  else:
    print(x)
    time.sleep(1) # lower the number the faster it will count down