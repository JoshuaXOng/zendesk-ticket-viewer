from database.zendeskcontroller import ZendeskController
from models.ticket import Ticket
from utilities.inpututils import InputUtils
import requests
from typing import List

class Display():
    """ Contains the visuals and logic in which the user is to interact with the system. """

    def __init__(self):
        self.zendesk_controller = ZendeskController()
    
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

            prompt = "Select thou option: "
            err_msg = "Please select an existing option from the table."
            command = InputUtils.inputOption(options, prompt, err_msg)

            if command == view_all_tickets:
                self._execViewAllTicketsOption()
            elif command == view_ticket_of_id:
                self._execViewTicketOfIdOption()

    def _execViewAllTicketsOption(self):
        """ The logic for the view all tickets option. """

        # If account has tickets, fetch tickets on first page.
        try: 
            ticket_count = self.zendesk_controller.fetchTicketCount()
            page_no = 1
            tickets, has_prev_page, has_next_page = self.zendesk_controller.fetchPageOfTickets(page_no)
        except requests.exceptions.HTTPError as e:
            print(e)
            return
        except requests.exceptions.RequestException:
            print("Zendesk API is unavailable")
            return

        if not ticket_count: 
            print("You have no tickets...")
            return
        
        # Display tickets on page and enter/show pagination controls.
        do = True
        while do or (has_prev_page or has_next_page):
            do = False
            
            print("\nYou have "+str(ticket_count)+" total tickets.")
            self._printTicketsOverview(tickets)
            print("Page "+str(page_no)+", "+str(len(tickets))+" tickets on this page")

            exit_paging = 0 
            prev = 1
            next_ = 2
            paging_options = [exit_paging]
            if has_prev_page:
                paging_options.append(prev)
                print("Select 1 to page back.")
            if has_next_page:
                paging_options.append(next_)
                print("Select 2 to page forward.")
            print("Select 0 to quit.")
            
            paging_option = InputUtils.inputOption(paging_options, "\nEnter a navigation option: ", "Please select a valid option.")
            try:
                if paging_option == exit_paging:
                    break
                elif paging_option == prev:
                    page_no -= 1
                    tickets, has_prev_page, has_next_page = self.zendesk_controller.fetchPageOfTickets(page_no)
                elif paging_option == next_:
                    page_no += 1
                    tickets, has_prev_page, has_next_page = self.zendesk_controller.fetchPageOfTickets(page_no)
            except requests.exceptions.HTTPError as e:
                print(e)
                return
            except requests.exceptions.RequestException:
                print("Zendesk API is unavailable")
                return

    def _execViewTicketOfIdOption(self):
        """ The logic for the view ticket of id option. """
        id_ = InputUtils.inputValidInt("Select thou id: ")   
        try:
            ticket = self.zendesk_controller.fetchTicketWithID(id_)
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.RequestException:
            print("Zendesk API is unavailable")
        else: 
            print("\n"+ticket.indepth())

    def _printTicketsOverview(self, tickets: List[Ticket]):
        """ Prints the overviews of the supplied list of tickets. """
        for ticket in tickets:
            print(ticket.overview())