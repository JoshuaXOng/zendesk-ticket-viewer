
class Ticket():
    """ Represents a Zendesk ticket. """

    def __init__(self, data: dict):
        """ Constructor.
        Decodes JSON data into a Zendesk ticket.
        :param data: JSON formatted data
        :raises KeyError: if id, status, ..., description keys are not found in data
        """
        try:
            self.id = data["id"] 
            self.status = data["status"]
            self.subject = data["subject"]
            self.created_at = data["created_at"]
            self.requester_id = data["requester_id"]
            self.description = data["description"]
        except KeyError as e:
            raise KeyError("Ticket could not get decoded properly - perhaps data is malformed.")

    def __str__(self) -> str: 
        return str(self.id)+" || "+self.status+" || "+str(self.requester_id)+" || "+self.created_at+" || "+self.subject+" || "+self.description