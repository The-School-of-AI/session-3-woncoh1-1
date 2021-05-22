from fractions import Fraction
from decimal import Decimal
from collections import Counter

def encoded_from_base10(number: int, base: int, digit_map: str):  
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    if number == 0:
        return [0]
    for count in Counter(digit_map).values():
        if count > 1:
            raise ValueError("Invalid digit_map: repeating digits not allowed in digit_map")
    sign = -1 if number < 0 else 1
    number *= sign
    digits = []
    while number > 0:
        number, remainder = divmod(number, base)
        digits.insert(0, remainder)
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")
    encoding = ''.join([digit_map[digit] for digit in digits])
    if sign == -1:
        encoding = '-' + encoding
    return encoding


def float_equality_testing(a: float, b: float):  
    '''
    This function emulates the ISCLOSE method from the MATH module, but you can't use this function
    We are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def manual_truncation_function(f_num: float):  
    '''
    This function emulates python's MATH.TRUNC method:
    - It ignores everything after the decimal point. 
    - It must check whether f_num is of correct type before proceed. 
    - You can use inbuilt constructors like int, float, etc.
    '''
    if not isinstance(f_num, float):
        raise ValueError("Invalid f_num: f_num should be a 32-bit floating point number")
    return f_num.__int__()


def manual_rounding_function(f_num: float):  
    '''
    This function emulates python's inbuild ROUND function. 
    You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num == 0:
        return 0
    str_int = str(f_num).split('.')[0]
    is_negative = str_int[0] == '-'
    first_decimal_place = len(str_int) - 1 if is_negative else len(str_int)
    first_decimal_value = Decimal(f_num).as_tuple().digits[first_decimal_place]
    if first_decimal_value < 5:
        return manual_truncation_function(f_num)
    else:
        if is_negative:
            return manual_truncation_function(f_num - 0.5)
        else:
            return manual_truncation_function(f_num + 0.5)


def rounding_away_from_zero(f_num):  
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if f_num == 0:
        return 0
    str_int, str_dec = str(f_num).split('.')
    if str_dec == '0':
        return str_int
    is_negative = str_int[0] == '-'
    first_decimal_place = len(str_int) - 1 if is_negative else len(str_int)
    first_decimal_value = Decimal(f_num).as_tuple().digits[first_decimal_place]
    if is_negative:
        return manual_truncation_function(f_num - 1)
    else:
        return manual_truncation_function(f_num + 1)
