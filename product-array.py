'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# empty list to add products
# multiplying products of all numbers to left and right will get final product
# empty lists for left and right products
# left list and right list will have at each index products
# for left list loop through length of list
    # at start index make the product equal to 1
    # for following index get the num at the same index and multiply by previous product
# for right list loop backwards to build up
    # at start index make product 1
    # for following index...
# loop through len of nums
    # multiply the left and right products at current index and add to empty list

class Solution:
    '''
    >>> solution = Solution()
    >>> nums = [1,2,3,4]
    >>> solution.productExceptSelf(nums)
    [24, 12, 8, 6]
    '''
    def productExceptSelf(self, nums):
        products = []
        left = [None] * len(nums)
        right = [None] * len(nums)
        for i in range(len(left)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1] * nums[i-1]
        for i in range(len(right)-1, -1, -1):
            if i == len(right) - 1:
                right[i] = 1
            else:
                right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            products.append(left[i] * right[i])
        return products

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')        