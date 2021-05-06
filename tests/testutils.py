import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from unittest import main, TestCase
from unittest.mock import patch
from utilities.utils import Utils

class TestUtils(TestCase):
    """ A group of unit tests for the methods contained within Utils. """

    def test_resizeString(self):
        empty_space = 20*" "
        self.assertEqual("0123456789"+empty_space, Utils.resizeString("0123456789"))
        self.assertEqual("012345678901234567890123456...", Utils.resizeString("0123456789012345678901234567890123456789"))

    def test_inputValidInt(self):
        mock_input = ["y","7"]
        with patch('builtins.input', side_effect=mock_input):
            result = Utils.inputValidInt("Mocking an input: ")
            self.assertEqual(7,result)

    def test_inputOneOrZero(self):
        mock_input = ["2","1"]
        with patch('builtins.input', side_effect=mock_input):
            result = Utils.inputOneOrZero("Mocking an input: ")
            self.assertEqual(1,result)

if __name__ == "__main__":
    unittest.main(buffer=True)