
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
