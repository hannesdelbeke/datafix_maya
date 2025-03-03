from datafix.core import Validator, active_session


class GreetingsValidator(Validator):
    """check if string is a greeting"""
    required_type = str

    # TODO hookup sample action node

    def logic(self, data):
        accepted_greetings = ['hello', 'hi', 'hey']
        if not data.lower() in accepted_greetings:
            raise Exception(f'{data} is not a valid greeting, try {accepted_greetings}')