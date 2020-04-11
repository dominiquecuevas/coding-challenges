# result variable set to 0
# loop through reversed num string and enumerate turn into ints
    # set 0 new num variable
    # add 0's for each idx
    # loop through reversed second num
        # add to num variable
# return result of multiplying 2 new num variables together and convert to string

def get_int(num):
    new_num = 0
    for idx, char in enumerate(num):
        new_char = char + str(0) * (len(num) - idx - 1)
        new_num += int(new_char)
    return new_num

def multiply_strings(num1, num2):
    '''
    >>> num1 = '2'
    >>> num2 = '3'
    >>> multiply_strings(num1, num2)
    '6'
    >>> num1 = '123'
    >>> num2 = '456'
    >>> multiply_strings(num1, num2)
    '56088'
    '''

    int_num1 = get_int(num1)
    int_num2 = get_int(num2)

    return str(int_num1 * int_num2)

import doctest
if doctest.testmod(verbose=True).failed == 0:
    print('all tests passed')