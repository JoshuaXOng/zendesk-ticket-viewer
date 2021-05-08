import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from unittest import main, TestCase
from unittest.mock import patch
from utilities.stringutils import StringUtils

class TestStringUtils(TestCase):
    """ A group of unit tests for the methods contained within StringUtils. """

    def test_resizeString(self):
        
        # Test short string gets sized up.
        empty_space = 20*" "
        self.assertEqual("0123456789"+empty_space, StringUtils.resizeString("0123456789",30))

        # Test perfect length string does not change.
        self.assertEqual("012345678901234567890123456789", StringUtils.resizeString("012345678901234567890123456789",30))

        # Test long string gets sized down.
        self.assertEqual("012345678901234567890123456...", StringUtils.resizeString("0123456789012345678901234567890123456789",30))

if __name__ == "__main__":
    unittest.main(buffer=True)