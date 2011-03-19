import locale

def format_number(number):
    """Formats the input number in accordance to localization, with thousand
    delimiters and fraction delimiters"""
    if locale.setlocale(locale.LC_ALL, '') == 'C':
        locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.format("%d", number, True)