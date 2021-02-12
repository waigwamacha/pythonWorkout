from decimal import Decimal 

class HourTooLowError(Exception): pass
class HourTooHighError(Exception): pass

def calculate_tax(amount, state, hour):
    """ 
    calculates the tax for Freedonia states
    """
    rates = {
            'Chico': 0.5, 
            'Groucho': 0.7, 
            'Harpo': 0.5, 
            'Zeppo': 0.4
            }

    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')

    if hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')

    def time_percentage(hour): 
        return hour / 24

    def calculate_tax(amount, state, hour):
        return amount + (amount * rates[state] * time_percentage(hour))

