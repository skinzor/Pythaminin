## Examples ##

class IncorrectValueError(Exception):

    def __init__(self, value):
        message = f'Bad Value:{value}'
        super().__init__(message)

value = 69+2

if value != 69:
    raise IncorrectValueError(value)

### Don't do these
class custom_exception(Exception):
    pass
raise custom_exception()

raise Exception('Bruh!')
