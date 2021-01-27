def myxml(parent, child='', **kwargs):
    """
    function that takes a numberof arguments and prints an xml output
    """
    pair = ''.join([f"{key}='{value}'" for key, value in kwargs.items()])
    print(f'<name, {pair}>{child}</name>')

myxml('parent', 'child', a=1, b=3)