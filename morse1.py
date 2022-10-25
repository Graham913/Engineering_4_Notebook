


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