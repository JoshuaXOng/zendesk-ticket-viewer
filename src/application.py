from display import Display

class Application():
    """ The entry point of the ticket viewer application. """

    @staticmethod
    def main():
        print("\nWELCOME TO JOSHUAXONG's ZENDESK TICKET VIEWER")
        display = Display()
        display.menu()
        print("\nGoodbye!\n")

if __name__ == "__main__":
    Application.main()