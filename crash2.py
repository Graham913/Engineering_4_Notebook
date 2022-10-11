#type:ignore
import time
import board
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led1 = digitalio.DigitalInOut(board.GP12)
led1.direction = digitalio.Direction.OUTPUT

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("")


    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9 or mpu.acceleration[1] < -9: 
        led1.value = True
    
    else:
        led1.value = False
        time.sleep(.5)