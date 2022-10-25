
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier



MORSE_CODE = { 'A':'.-', 'B':'-...',
      'C':'-.-.', 'D':'-..', 'E':'.',
      'F':'..-.', 'G':'--.', 'H':'....',
      'I':'..', 'J':'.---', 'K':'-.-',
      'L':'.-..', 'M':'--', 'N':'-.',
      'O':'---', 'P':'.--.', 'Q':'--.-',
      'R':'.-.', 'S':'...', 'T':'-',
      'U':'..-', 'V':'...-', 'W':'.--',
      'X':'-..-', 'Y':'-.--', 'Z':'--..',
      '1':'.----', '2':'..---', '3':'...--',
      '4':'....-', '5':'.....', '6':'-....',
      '7':'--...', '8':'---..', '9':'----.',
      '0':'-----', ', ':'--..--', '.':'.-.-.-',
      '?':'..--..', '/':'-..-.', '-':'-....-',
      '(':'-.--.', ')':'-.--.-', ' ':'/'}
while True:
  print('Enter Morse Code Message, or enter -q to quit:')
  message = input() 
  if message == "-q":
    break
  message = message.upper()
  doofinshmirtz = " "
  for letter in message:
    doofinshmirtz = doofinshmirtz + MORSE_CODE[letter] + " "
  print(doofinshmirtz)

  for perrytheplatypus in doofinshmirtz:
    if perrytheplatypus == ".":
      led.value = True
      time.sleep(dot_time)
      led.value = False
      time.sleep(between_taps)

    if perrytheplatypus == "-":
      led.value = True
      time.sleep(dash_time)
      led.value = False
      time.sleep(between_taps)

    if perrytheplatypus == " ":
      time.sleep(between_letters)

    if perrytheplatypus == "/":
      time.sleep(between_words)