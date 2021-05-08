import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from unittest import main, TestCase
from unittest.mock import patch
from utilities.stringutils import StringUtils

class TestStringUtils(TestCase):
    """ A group of unit tests for the methods contained within Utils. """

    def test_resizeString(self):
        empty_space = 20*" "
        self.assertEqual("0123456789"+empty_space, Utils.resizeString("0123456789"))
        self.assertEqual("012345678901234567890123456...", Utils.resizeString("0123456789012345678901234567890123456789"))

if __name__ == "__main__":
    unittest.main(buffer=True)