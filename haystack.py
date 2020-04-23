'''
base case is idx is equal to length of haystack
or base case is when the element at idx is needle
mutate the list and idx
'''
def find_needle(needle, haystack, idx=0):
    '''
    For example:

    >>> find_needle(5, [1, 3, 5, 2, 4])
    2
    >>> find_needle("hey", ["hey", "there", "you"])
    0
    >>> find_needle("you", ["hey", "there", "you"])
    2
    >>> find_needle("zork", ["foo", "bar", "baz"]) is None
    True
    '''
    if idx == len(haystack):
        return
    if needle == haystack[idx]:
        return idx
    return find_needle(needle, haystack, idx+1)

import doctest
if doctest.testmod(verbose=True).failed == 0:
    print('all tests passed')