def single_number(nums):
    """
    >>> single_number([2,2,1])
    1
    >>> single_number([4,1,2,1,2])
    4
    """
    
    nums.sort()
    i = 0
    while i < len(nums):
        if i+3 < len(nums) and nums[i] == nums[i+1]:
            i += 2
        elif i+2 < len(nums) and nums[i+1] == nums[i+2]:
            return nums[i]
        else:
            i += 2
            return nums[i]

def single_number_(nums):
    """
    >>> single_number_([2,2,1])
    1
    >>> single_number_([4,1,2,1,2])
    4
    """
    dict_nums = {}
    for i in nums:
        try:
            dict_nums.pop(i)
        except:
            dict_nums[i] = 1
    return dict_nums.popitem()[0]

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed!")