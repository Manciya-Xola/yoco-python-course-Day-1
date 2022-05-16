from ast import Try
from challenge1 import *
import unittest   # The test framework


class Test_ROT13(unittest.TestCase):
  
  def test_numbers(self):
    with self.assertRaises(WrongInputException):
      rot13('123456')

  def test_uppercaseLetters(self):
    self.assertEqual("URYYBJBEYQ", rot13('HELLOWORLD').upper())

  def test_lowercaseLetters(self):
    self.assertEqual("URYYBJBEYQ".lower(), rot13('helloworld'))

  def test_upperAndLowercase(self):
    self.assertEqual("URYYBJBEYQ".lower(), rot13('HELLOworld'))

  def test_containsSpace(self):
    self.assertEqual("URYYB JBEYQ".lower(), rot13('HELLO world'))

  def test_containsSpecialCharacters(self):
    with self.assertRaises(WrongInputException):
      rot13('HELLO "/ world')

  def test_mixNumbersUppercaseLowercase(self):
    with self.assertRaises(WrongInputException):
      rot13('hello World 123')
if __name__ == '__main__':
    unittest.main()
