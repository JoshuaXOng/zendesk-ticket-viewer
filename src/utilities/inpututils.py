from typing import List

class InputUtils():
    """ Contains various handy functions that relate to retrieving user input. """

    @staticmethod
    def inputOption(options: List[int], prompt: str, err_msg: str) -> int:
        """ Prompts the user to select an option contained within the supplied options. 
        :param options: the list of integer options that the user is able to select.
        :param prompt: the prompting message that is to be displayed to the user.
        :param err_msg: the message that is to be displayed upon invalid input. 
        :return: the option selected by the user. 
        """
        is_valid = False
        while not is_valid:
            try:
                command = int(input(prompt))
                if command not in options:
                    raise Exception()
                is_valid = True
            except:
                print(err_msg) 
        return command

    @staticmethod
    def inputValidInt(message: str) -> int:
        """ Prompts the user for a valid integer. 
        :param message: the prompting message that is displayed to the user.
        :return: the integer selected by the user.
        """
        is_valid = False
        while not is_valid:
            try:
                input_ = int(input(message))
                is_valid = True
            except ValueError as e:
                print(e) 
        return input_

    @staticmethod
    def inputOneOrZero(message: str) -> int:
        """ Prompts the user for the integers 0 or 1. 
        :message: the prompting message that is displayed to the user.
        :return: 0 or 1 depending on user selection.
        """
        is_valid = False
        while not is_valid:
            try:
                input_ = int(input(message))
                if not input_ == 0 and not input_ == 1:
                    raise ValueError 
                is_valid = True
            except ValueError:
                print("Please enter a 0 or a 1.") 
        return input_