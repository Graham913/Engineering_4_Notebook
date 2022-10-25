#type:ignore
import digitalio
import board
import time

for x in range(10, -1,-1):
  if x == 0:
    print("liftoff!")

  else:
    print(x)
    time.sleep(1)