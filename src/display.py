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
            tickets = self.zendeskController.fetchAllTickets()
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.RequestException:
            print("Zendesk API is unavailable")
        else:                
            print("\nYou have "+str(len(tickets))+" tickets.")
            for page_no, page_of_tickets in enumerate(Utils.paginateData(tickets),1):
                self._printTicketsOverview(page_of_tickets)
                print("Page "+str(page_no)+", "+str(len(page_of_tickets))+" tickets on this page")
                show_next = Utils.inputOneOrZero("\nNext page of tickets (yes: 1 / no: 0)?\n")
                if not show_next: break

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