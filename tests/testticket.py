import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from models.ticket import Ticket
from utilities.utils import Utils

class TestTicket(unittest.TestCase):
    """ A group of unit tests for the methods contained within Ticket. """

    test_json = {
        "id": 106,
        "status": "open",
        "subject": "Please test me",
        "created_at": "2000-10-31T04:34:05Z",
        "requester_id": "1337",
        "description": "Can thou give me a test",
        "dud_field": "Can thou give me a test"
    }
    test_ticket = Ticket(test_json)

    test_json_malformed = {
        "id": 106,
        "created_at": "2000-10-31T04:34:05Z",
        "description": "Can thou give me a test",
        "dud_field": "Can thou give me a test"
    }

    def test_overview(self):
        output = self.test_ticket.overview()
        resized_subject = Utils.resizeString(self.test_ticket.subject)
        self.assertEqual(output, 
            "|| ID: 106, Status: open || Subject: "+resized_subject+" || Requested at: 31 Oct 2000 04:34:05"
        )

    def test_indepth(self):
        output = self.test_ticket.indepth()
        self.assertEqual(output, 
            "|| ID: 106, Status: open || Subject: Please test me || Requested at: 31 Oct 2000 04:34:05 || Requested by: 1337\n\nCan thou give me a test"
        )

    def test_constructor(self):
        self.assertRaises(KeyError,Ticket,self.test_json_malformed)

if __name__ == "__main__":
    unittest.main()