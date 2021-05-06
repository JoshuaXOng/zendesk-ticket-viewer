
class Utils():
    """ Holds useful methods. """

    @staticmethod
    def resizeString(string: str) -> str:
        """ Resizes the string if longer/shorter than a certain length.
        If string is shorter, additional whitespaces will be added to increase length.
        If string is logner, it will get truncated to match a certain length.
        """
        desired_length = 30
        if len(string) > desired_length:
            string = string[:desired_length-3]
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


