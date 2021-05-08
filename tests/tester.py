import unittest
from testinpututils import TestInputUtils
from teststringutils import TestStringUtils
from testticket import TestTicket

class Tester(unittest.TestCase):
    """ Aggregates tests -- does not implement any additional itself. """

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestInputUtils())
        suite.addTest(TestStringUtils())
        suite.addTest(TestTicket())
        return suite

if __name__ == "__main__":
    unittest.main(buffer=True)

