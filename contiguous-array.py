# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# [0, 0, 1, 0, 0, 0, 1, 1] => 6

# possible arrays all start with the 0 index or 2nd to last index

class Solution:
    def findMaxLength(self, nums):
        '''
        >>> nums = [0, 0, 1, 0, 0, 0, 1, 1]
        >>> solution = Solution()
        >>> solution.findMaxLength(nums)
        6
        >>> nums = [0,1,0]
        >>> solution.findMaxLength(nums)
        2
        '''
        dict_count_idx = {}
        sub_array = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                counter += -1
            if counter == 0:
                sub_array = i + 1
            if counter in dict_count_idx:
                sub_array = max(sub_array, i-dict_count_idx[counter])
            else:
                dict_count_idx[counter] = i
        return sub_array

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')