def find_duplicate(lst):
    '''optimize for space
    >>> lst = [5, 4, 3, 2, 5, 2]
    >>> find_duplicate(lst)
    5
    '''
    for idx1 in range(len(lst)-1):
        for idx2 in range(1, len(lst)):
            if lst[idx1] == lst[idx2]:
                return lst[idx1]

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')