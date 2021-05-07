from datetime import datetime
from typing import TypeVar, Generic
from utilities.stringutils import StringUtils

T = TypeVar("T")

class Ticket(Generic[T]):
    """ Represents a Zendesk ticket. """

    def __init__(self, data: dict[str,T]):
        """ Constructor.
        Decodes JSON data into a Zendesk ticket.
        :param data: JSON formatted data of a Zendesk ticket.
        :raises KeyError: if id, status, subject, created_at, requester_id and description keys are not found in data.
        """
        try:
            self.id = data["id"] 
            self.status = data["status"]
            self.subject = data["subject"]
            self.created_at = data["created_at"]
            self.requester_id = data["requester_id"]
            self.description = data["description"]
        except KeyError as e:
            raise KeyError("Ticket could not get decoded properly.")

    def overview(self) -> str:
        """ Returns an overview of the ticket's details. """
        output = "|| ID: {id_}, Status: {status} || Subject: {sub} || Requested at: {date_req}"
        subject = StringUtils.resizeString(self.subject, 30)
        try:
            creation_date = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y %H:%M:%S")
        except:
            creation_date = self.created_at
        formatted_output = output.format(id_=self.id, status=self.status, sub=subject, date_req=creation_date)
        return formatted_output

    def indepth(self) -> str:
        """ Returns an indepth look of the ticket's details. """
        output = "|| ID: {id_}, Status: {status} || Subject: {sub} || Requested at: {date_req} || Requested by: {req_id}\n\n{desc}"
        try:
            creation_date = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y %H:%M:%S")
        except:
            creation_date = self.created_at
        formatted_output = output.format(id_=self.id, status=self.status, sub=self.subject, date_req=creation_date, req_id=self.requester_id, desc=self.description)
        return formatted_output

    def __str__(self) -> str: 
        return str(self.id)+" || "+self.status+" || "+str(self.requester_id)+" || "+self.created_at+" || "+self.subject+" || "+self.description