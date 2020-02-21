def contains_duplicates(lst):
    """
    Runtime is O(n log n). Sorting is O(n log n) and the loop is O(n) 
    >>> contains_duplicates([1,2,3,1])
    True
    >>> contains_duplicates([1,2,3,4])
    False
    """
    lst.sort()
    for idx in range(1, len(lst)):
        if lst[idx-1] == lst[idx]:
            return True
    return False

def contains_duplicates_sets(lst):
    """
    >>> contains_duplicates_sets([1,2,3,1])
    True
    >>> contains_duplicates_sets([1,2,3,4])
    False
    """
    lst_set = set(lst)
    if len(lst_set) != len(lst):
        return True
    return False

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed.")