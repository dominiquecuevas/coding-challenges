def rotate_list(lst, steps):
    """
    >>> rotate_list([1, 2, 3, 4, 5, 6, 7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate_list([-1, -100, 3, 99], 2)
    [3, 99, -1, -100]
    >>> rotate_list([1,2], 3)
    [2, 1]
    """
    new_list = [0] * len(lst)
    for idx in range(len(lst)):
        new_idx = idx + steps
        if new_idx >= len(lst):
            while new_idx >= len(lst):
                new_idx -= len(lst)
            new_list[new_idx] = lst[idx]
        else:
            new_list[new_idx] = lst[idx]
    return new_list

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print('All tests passed')