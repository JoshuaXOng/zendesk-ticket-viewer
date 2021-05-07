
class StringUtils():
    """ Holds useful methods that operate on strings. """

    @staticmethod
    def resizeString(string: str, desired_length: int) -> str:
        """ Resizes the string if longer/shorter than a certain length.
        If string is shorter, additional whitespaces will be added to increase length.
        If string is logner, it will get truncated to match a certain length.
        :param string: the string that is to be resized.
        :param desired_length: the size that is to be attained.
        :return: the modified string.
        """
        if len(string) > desired_length:
            string = string[:desired_length-3]
            string += "..."
        else: 
            no_whitespaces = desired_length - len(string)
            string += " "*no_whitespaces
        return string




