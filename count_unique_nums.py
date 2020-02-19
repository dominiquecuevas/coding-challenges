def return_len_no_dupes(nums):
    """
    >>> return_len_no_dupes([1,1,2])
    2
    >>> return_len_no_dupes([0,0,1,1,1,2,2,3,3,4])
    5
    """
    i = 0   # start at 0, keeps track of index to compare the loop to. +1 for the 
    for idx in range(1, len(nums)):  # start at 1 idx then loop to end
        if nums[idx] != nums[i]:  # found unique number
            i += 1  # iterate i
            nums[i] = nums[idx]  # set the next item to the value of the new num
    
    return i + 1

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if result.failed == 0:
        print("ALL TESTS PASSED")