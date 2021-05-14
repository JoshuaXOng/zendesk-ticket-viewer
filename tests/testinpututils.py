import sys, os
sys.path.insert(0, os.path.abspath('.\src'))
import unittest
from unittest import main, TestCase
from unittest.mock import patch
from utilities.inpututils import InputUtils

class TestInputUtils(TestCase):
    """ A group of unit tests for the methods contained within InputUtils. """

    def test_inputOption(self):
        
        # Test that inputOption() rejects invalid options 2 and -1, then accepts 4.
        mock_input = ["2", "-1", "4"]
        with patch('builtins.input', side_effect=mock_input):
            dummy_options = [0, 4, 10]
            dummy_text = "A prompt message and an error message."
            result = InputUtils.inputOption(dummy_options, dummy_text, dummy_text)
            self.assertEqual(4, result)
        
        # Test that inputOption() works first try.
        mock_input = ["2", "3", "4"]
        with patch('builtins.input', side_effect=mock_input):
            dummy_options = [2, 4, 10]
            dummy_text = "A prompt message and an error message."
            result = InputUtils.inputOption(dummy_options, dummy_text, dummy_text)
            self.assertEqual(2, result)

    def test_inputValidInt(self):

        # Test that inputValidInt() rejects a letter and accepts 7.
        mock_input = ["y", "7"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.inputValidInt("Mocking an input: ")
            self.assertEqual(7, result)

        # Test that inputValidInt() rejects a double and accepts an integer.
        mock_input = ["4.4", "9"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.inputValidInt("Mocking an input: ")
            self.assertEqual(9, result)

    def test_inputOneOrZero(self):
        mock_input = ["0.0", "2", "1"]
        with patch('builtins.input', side_effect=mock_input):
            result = InputUtils.inputOneOrZero("Mocking an input: ")
            self.assertEqual(1, result)

if __name__ == "__main__":
    unittest.main(buffer=True)