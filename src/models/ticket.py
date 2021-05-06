
class Ticket():
    """ Represents a Zendesk ticket.
    """

    def __init__(self, data: dict):
        try:
            self.id = data["id"] 
            self.status = data["status"]
            self.subject = data["subject"]
            self.created_at = data["created_at"]
            self.requester_id = data["requester_id"]
            self.description = data["description"]
        except KeyError as e:
            #e.message... raise 
            raise KeyError("Ticket could not get decoded properly - perhaps data is malformed.")

    def __str__(self) -> str: 
        return str(self.id)+" || "+self.status+" || "+str(self.requester_id)+" || "+self.created_at+" || "+self.subject+" || "+self.description