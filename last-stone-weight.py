# while loop to check if length of list > 1
# sort list
# starting at 2 largest
# compare the 2 numbers for the remaining weight or if equal then pop both destroy
# if there is a stone in the list, return the weight
# if no stones return 0



class Solution:
    '''
    >>> solution = Solution()
    >>> stones = [2,7,4,1,8,1]
    >>> solution.lastStoneWeight(stones)
    1
    '''
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            large = stones[-1]
            small = stones[-2]
            if large - small == 0:
                stones.pop()
                stones.pop()
            else:
                stones.pop()
                stones[-1] = large - small
        if len(stones):
            return stones[0]
        else:
            return 0

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')