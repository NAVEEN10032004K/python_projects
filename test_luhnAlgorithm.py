from luhnAlgorithm import card_number_checker

def test_luhnalgorithm():
  # Valid card numbers
  assert card_number_checker(card_number='4532015112830366') == 0
  assert card_number_checker(card_number='6011514433546201') == 0
  assert card_number_checker(card_number='371449635398431') == 0
  assert card_number_checker(card_number='5555555555554444') == 0

  # Invalid card numbers 

  assert card_number_checker(card_number='4532015112830365') > 0
  assert card_number_checker(card_number='7992739871') > 0
  assert card_number_checker(card_number='1234567890123456') > 0

  # Edge cases
  assert card_number_checker(card_number='0') == 0
  assert card_number_checker(card_number='18') == 0 
  assert card_number_checker(card_number='0000000000000000') == 0 
  assert card_number_checker(card_number='1111111111111111') > 0 
