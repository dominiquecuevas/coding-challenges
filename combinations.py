def combinations(n, k):
    """
    Leetcode 77. Given two integers n and k, 
    return all possible combinations of k numbers out of 1 ... n.
    """
    largest = n if n >= k else k
    if largest == 1:
        return [[1]]
    nums = range(1, largest+1)
    pointer = 0
    result = []
    while pointer <= len(nums) - 1:
        for i in range(pointer+1, len(nums)):
            result.append([nums[pointer], nums[i]])
        pointer +=1


    return result