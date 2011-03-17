"""Convert to and from Roman numerals

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

import re

#Define exceptions
class RomanError(Exception):
    """
    General error for roman numerals
    # PyUML: Do not remove this line! # XMI_ID:_EH19YhEREd-LgJ4IxcJkTA
    """
    pass
class OutOfRangeError(RomanError):
    """
    Thrown then the requested value os out of the roman numeral range
    # PyUML: Do not remove this line! # XMI_ID:_EH19YxEREd-LgJ4IxcJkTA
    """
    pass
class NotIntegerError(RomanError):
    """
    Thrown when input is not an integer
    # PyUML: Do not remove this line! # XMI_ID:_EH19ZBEREd-LgJ4IxcJkTA
    """
    pass
class InvalidRomanNumeralError(RomanError):
    """
    Thrown when the input is not a roman numeral
    # PyUML: Do not remove this line! # XMI_ID:_EH2kcBEREd-LgJ4IxcJkTA
    """
    pass

#Define digit mapping
ROMAN_NUMERAL_MAP = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(number):
    """convert integer to Roman numeral"""
    if number == 0:
        return "N"
    if not (0 < number < 3999):
        raise OutOfRangeError, "number out of range (must be 1..3999)"
    if int(number) != number:
        raise NotIntegerError, "non-integers can not be converted"

    result = ""
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while number >= integer:
            result += numeral
            number -= integer
    return result

#Define pattern to detect valid Roman numerals
ROMAN_NUMERAL_PATTERN = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    ''' , re.VERBOSE)

def from_roman(roman_numeral):
    """convert Roman numeral to integer"""
    if not roman_numeral:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if roman_numeral == "N":
        return 0
    if not ROMAN_NUMERAL_PATTERN.search(roman_numeral):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % \
        roman_numeral

    result = 0
    index = 0
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while roman_numeral[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
