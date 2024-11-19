from caeser_cipher import caeser_cipher

def test_caserCipher():
  assert caeser_cipher(message='Hello', shift=3) == 'Khoor'
  assert caeser_cipher(message='world', shift= -3) == 'tloia'
  assert caeser_cipher(message='xyz', shift=3) == 'abc'
  assert caeser_cipher(message='HelloWorld', shift=5) == 'MjqqtBtwqi'
  assert caeser_cipher(message='HELLO', shift=0) == 'HELLO'
  assert caeser_cipher(message='Hello, World!', shift=4) == 'Lipps, Asvph!'
  assert caeser_cipher(message='ABC', shift=29) == 'DEF'
  assert caeser_cipher(message='XYZ', shift= -55) == 'UVW'
  assert caeser_cipher(message='', shift=5) == ''
  assert caeser_cipher(message='ABCDEFGHIJKLMNOPQRSTUVWXYZ', shift=5) == 'FGHIJKLMNOPQRSTUVWXYZABCDE'
  assert caeser_cipher(message='FGHIJKLMNOPQRSTUVWXYZABCDE', shift=-5) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  assert caeser_cipher(message='abcdefghijklmnopqrstuvwxyz', shift=5) == 'fghijklmnopqrstuvwxyzabcde'
  assert caeser_cipher(message='fghijklmnopqrstuvwxyzabcde', shift=-5) == 'abcdefghijklmnopqrstuvwxyz'

