
class Utils():

    @staticmethod
    def limitStringLength(string: str) -> str:
        max_length = 30
        if len(string) > max_length:
            string = string[:max_length]
            string += "..."
        return string

