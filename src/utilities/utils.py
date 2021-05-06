
class Utils():
    """ Holds useful methods. """

    @staticmethod
    def limitStringLength(string: str) -> str:
        """ Truncates the string if longer than a certain length. """
        max_length = 30
        if len(string) > max_length:
            string = string[:max_length]
            string += "..."
        return string

    @staticmethod
    def resizeString(string: str) -> str:
        """ Resizes the string if longer/shorter than a certain length.
        If string is shorter, additional whitespaces will be added to increase length.
        If string is logner, it will get truncated to match a certain length.
        """
        desired_length = 30
        if len(string) > desired_length:
            string = string[:desired_length-2]
            string += "..."
        else: 
            no_whitespaces = desired_length - len(string)
            string += " "*no_whitespaces
        return string

    @staticmethod
    def inputValidInt(message: str) -> int:
        """ Prompts the user for a valid integer. """
        isValid = False
        while not isValid:
            try:
                input_ = int(input(message))
                isValid = True
            except ValueError as e:
                print(e) 
        return input_

    @staticmethod
    def inputOneOrZero(message: str) -> int:
        """ Prompts the user for the integers 0 or 1. """
        isValid = False
        while not isValid:
            try:
                input_ = int(input(message))
                if not input_ == 0 and not input_ == 1:
                    raise ValueError 
                isValid = True
            except ValueError:
                print("Please enter a 0 or a 1") 
        return input_

    @staticmethod
    def paginateData(lst: list) -> list:
        """ Returns a portion of the supplied list. """
        no_items = 25
        for start in range(0,len(lst),no_items):
            end = start+no_items
            try:
                items_on_page = lst[start:end]
            except IndexError:
                items_on_page = lst[start:]
            yield items_on_page
