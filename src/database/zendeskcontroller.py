
class ZendeskController():
    """ Medaites the retreval and return of JSON data from Zendesk API. """

    def __init__(self):
        self.username = "joshuaong2000@gmail.com/token"
        self.password = "4gPQcPElcbFL02aqvbvTcxSzKm62oUZRuUuKPHmr"

    def fetchAllTickets(self) -> dict:
        """ Returns the JSON data from sending a get request to Zendesk API's tickets endpoint.
        :raises HTTPError: if the request encounters a 404, 401, etc. type error
        :raises RequestException: a catch all for request exceptions
        :return: a dictionary representing the JSON data of the response
        """
        tickets_url = "https://joshuaxong.zendesk.com/api/v2/tickets.json"
        try:
            response = requests.get(tickets_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise
        return response.json()
        
    def fetchTicketWithID(self, id_: int) -> dict:
        """ Returns the JSON data from sending a get request to Zendesk API's tickets endpoint.
        This request will only fetch a ticket of specific id.
        :raises HTTPError: if the request encounters a 404, 401, etc. type error
        :raises RequestException: a catch all for request exceptions
        :return: a dictionary representing the JSON data of the response
        """
        ticket_url = "https://joshuaxong.zendesk.com/api/v2/tickets/"+str(id_)+".json"
        try:
            response = requests.get(ticket_url, auth=(self.username, self.password))
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise
        except requests.exceptions.RequestException:
            raise
        return response.json()
        