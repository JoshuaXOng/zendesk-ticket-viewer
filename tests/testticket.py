import sys, os
sys.path.insert(0,os.path.abspath('.\src'))
import unittest
from models.ticket import Ticket
from utilities.stringutils import StringUtils

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

    test_json_2 = {
        "id": 34,
        "status": "open",
        "subject": "Please test me 2",
        "created_at": "2077-05-20T07:15:00Z",
        "requester_id": "23854720435",
        "description": "Test me"
    }
    test_ticket_2 = Ticket(test_json_2)

    test_json_malformed = {
        "id": 106,
        "created_at": "2000-10-31T04:34:05Z",
        "description": "Can thou give me a test",
        "dud_field": "Can thou give me a test"
    }

    def test_overview(self):
        # This test assumes StringUtils.resizeString() works correctly.

        output = self.test_ticket.overview()
        resized_subject = StringUtils.resizeString(self.test_ticket.subject, 30) 
        self.assertEqual(output, "|| ID: 106, Status: open || Subject: "+resized_subject+" || Requested at: 31 Oct 2000 04:34:05")

        output = self.test_ticket_2.overview()
        resized_subject = StringUtils.resizeString(self.test_ticket_2.subject, 30) 
        self.assertEqual(output, "|| ID: 34, Status: open || Subject: "+resized_subject+" || Requested at: 20 May 2077 07:15:00")

    def test_indepth(self):
        
        output = self.test_ticket.indepth()
        self.assertEqual(output, "|| ID: 106, Status: open || Subject: Please test me || Requested at: 31 Oct 2000 04:34:05 || Requested by: 1337\n\nCan thou give me a test")

        output = self.test_ticket_2.indepth()
        self.assertEqual(output, "|| ID: 34, Status: open || Subject: Please test me 2 || Requested at: 20 May 2077 07:15:00 || Requested by: 23854720435\n\nTest me")

    def test_constructor(self):
        self.assertRaises(KeyError, Ticket, self.test_json_malformed)

if __name__ == "__main__":
    unittest.main()