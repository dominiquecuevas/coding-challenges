def combinations(n, k):
    """
    Leetcode 77. Given two integers n and k, 
    return all possible combinations of k numbers out of 1 ... n.
    """
    # create a set of nums
    # turn set into list
    # have pointer to 0 index, then loop through list
    # increment pointer
    if n >= k:
        largest = n
    else:
        largest = k
    nums = range(1, largest+1)
    pointer = 0
    result = []
    while pointer < len(nums) - 1:
        for i in range(pointer+1, len(nums)):
            result.append([nums[pointer], nums[i]])
        pointer +=1


    return result