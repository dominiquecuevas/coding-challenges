class Solution:
    def smallerNumbersThanCurrent(self, nums):
        nums_sorted = sorted(nums)
        result = [None] * len(nums)
        for idx, num in enumerate(nums):
            result[idx] = nums_sorted.index(num)
        return result