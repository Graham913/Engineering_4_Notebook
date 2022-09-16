#type:ignore
import board
import digitalio

led = digitalio.DigitalInOut(board.GP18)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        led.value = True
    led.value = False