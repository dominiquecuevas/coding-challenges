# make zero variable move
# add up direction making left -1 for each amount and +1 for right
    # for loop and inc/decrement product of left/right and amount to move variable
# make string into list
# 'abcdef' > shift right by 2, reassign index to 2 that are to its left
# 'efabcd' < take current index reassign to left
# 'cdefab' shift left by 2
# but problem is the character changes for when we need to copy it
    # so make a new list with length of string list


def string_shifts(string, shifts):
    '''
    >>> string = "abc"
    >>> shifts = [[0,1],[1,2]]
    >>> string_shifts(string, shifts)
    'cab'
    >>> string = "abcdefg"
    >>> shifts = [[1,1],[1,1],[0,2],[1,3]]
    >>> string_shifts(string, shifts)
    'efgabcd'
    >>> string = 'abcdef'
    >>> shifts = [[0, 10], [1, 1], [0, 2]]
    >>> string_shifts(string, shifts)
    'fabcde'
    '''
    string_list = list(string)
    shifted = [None] * len(string_list)
    move = 0    # (-) for total left shifts and (+) for right
    # add up all the total shifts to increment move variable
    for shift in shifts:
        direction, steps = shift
        if direction == 0:
            move -= steps
        else:
            move += steps
    # if moving to the right, find the element to copy from left into new shifted list
    if move > 0:
        copy = -move    # copy the element X moves to the left
        # when the number of moves is greater than the length
        # need to revise the copy number to the remainder, using modulo
        # to add copy increments to string_list idx 
        while abs(copy) > len(string_list):
            copy = len(string_list) % copy
        for i in range(len(string_list)):
            shifted[i] = string_list[i+copy]
        return ''.join(shifted)
    elif move < 0:
        copy = -move
        # copy over the element X moves to the right
        # find the modulo of the negative length and copy number
        # add to negative indexes
        while abs(copy) > len(string_list):
            copy = -len(string_list) % copy
        for i in range(-len(string_list), 0):
            shifted[i] = string_list[i+copy]
        return ''.join(shifted)
    else:
        return string

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')