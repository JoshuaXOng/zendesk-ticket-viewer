import requests
from models.ticket import Ticket

class ZendeskController():
    """ Medaites the retreval and return of JSON data from Zendesk API. """

    def __init__(self):
        self.username = "joshuaong2000@gmail.com/token"
        self.password = "4gPQcPElcbFL02aqvbvTcxSzKm62oUZRuUuKPHmr"

    def fetchPageOfTickets(self, page_no) -> ([Ticket], bool):
        """ Returns the tickets on a specific page and checks whether there is a next page """
        
        tickets_url = "https://joshuaxong.zendesk.com/api/v2/tickets.json?per_page=25&page="+str(page_no)
        try:
            response = requests.get(tickets_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        tickets = []
        for entry in response_json["tickets"]:
            tickets.append(Ticket(entry))

        if response_json["next_page"]:
            has_next_page = True
        else:
            has_next_page = False

        return tickets, has_next_page

    def fetchTicketCount(self) -> int:
        """ Returns the number of tickets in the account. """

        tickets_url = "https://joshuaxong.zendesk.com/api/v2/tickets/count.json?"
        try:
            response = requests.get(tickets_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        count = response_json["count"]["value"]
        return count

    def fetchAllTickets(self) -> [Ticket]:
        """ Returns the tickets from sending a get request to Zendesk API's tickets endpoint.
        :raises HTTPError: if the request encounters a 404, 401, etc. type error
        :raises RequestException: a catch all for request exceptions
        :return: a list of tickets representing the JSON data of the response
        """

        tickets_url = "https://joshuaxong.zendesk.com/api/v2/tickets.json?"
        try:
            response = requests.get(tickets_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        tickets = []
        for entry in response_json["tickets"]:
            tickets.append(Ticket(entry))

        return tickets
        
    def fetchTicketWithID(self, id_: int) -> Ticket:
        """ Returns the ticket from sending a get request to Zendesk API's tickets endpoint.
        This request will only fetch a ticket of specific id.
        :raises HTTPError: if the request encounters a 404, 401, etc. type error
        :raises RequestException: a catch all for request exceptions
        :return: a ticket representing the JSON data of the response
        """
        
        ticket_url = "https://joshuaxong.zendesk.com/api/v2/tickets/"+str(id_)+".json"
        try:
            response = requests.get(ticket_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise

        response_json = response.json()
        entry = response_json["ticket"]
        
        return Ticket(entry)
        