from database.zendeskcontroller import ZendeskController
from models.ticket import Ticket
from utilities.utils import Utils
import requests

class Display():
    """ Contains the visuals and logic in which the user is to interact with the system. """

    def __init__(self):
        self.zendeskController = ZendeskController()
    
    def menu(self):
        """ Runs the user interface of the ticket viewer application. """

        view_all_tickets = 1
        view_ticket_of_id = 2
        exit_ = 3
        options = [view_all_tickets, view_ticket_of_id, exit_]
        command = -1
        while command != exit_:

            print(
                """ 
                OPTIONS:
                -------------------------------------
                | 1. View all tickets               |
                | 2. View ticket of certain id      | 
                | 3. Exit                           |
                -------------------------------------
                """
            )

            command = self._promptOptionSelection(options) 

            if command == view_all_tickets:
                self._exec_view_all_tickets_option()
            elif command == view_ticket_of_id:
                self._exec_view_ticket_of_id_option()
    
    def _promptOptionSelection(self, options: [int]) -> int:
        """ Prompts the user to select on of the supplied options. """
        isValid = False
        while not isValid:
            try:
                command = int(input("Select thou option: "))
                if command not in options:
                    raise 
                isValid = True
            except:
                print("Please select an existing option from the table.") 
        return command

    def _exec_view_all_tickets_option(self):
        """ The logic for the view all tickets option. """
        
        try:
            ticket_count = self.zendeskController.fetchTicketCount()
            print("\nYou have "+str(ticket_count)+" tickets.")
            if ticket_count:
                page_no = 0
                has_next_page = True
                while has_next_page:
                    if page_no > 0: 
                        if not Utils.inputOneOrZero("\nNext page of tickets (yes: 1 / no: 0)? "): break
                    page_no += 1
                    tickets, has_next_page = self.zendeskController.fetchPageOfTickets(page_no)
                    self._printTicketsOverview(tickets)
                    print("Page "+str(page_no)+", "+str(len(tickets))+" tickets on this page")
            else:
                print("You have no tickets...")
                
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.RequestException:
            print("Zendesk API is unavailable")

    def _exec_view_ticket_of_id_option(self):
        """ The logic for the view ticket of if option. """
        id_ = Utils.inputValidInt("Select thou id: ")   
        try:
            ticket = self.zendeskController.fetchTicketWithID(id_)
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.RequestException:
            print("Zendesk API is unavailable")
        else: 
            print("\n"+ticket.indepth())

    def _printTicketsOverview(self, tickets: [Ticket]):
        """ Prints the supplied list of tickets in a decent manner. """
        for ticket in tickets:
            print(ticket.overview())