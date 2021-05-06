import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from unittest import main, TestCase
from unittest.mock import patch
from display import Display
from models.ticket import Ticket

class TestDisplay(TestCase):
    """ A group of unit tests for the methods contained within Ticket. """

    def test_promptOptionSelection(self):
        test_display = Display()
        mock_input = ["4","3"]
        with patch('builtins.input', side_effect=mock_input):
            result = test_display._promptOptionSelection([1,2,3]) 
            self.assertEqual(3,result)

if __name__ == "__main__":
    unittest.main(buffer=True)