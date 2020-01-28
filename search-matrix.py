class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        nested loop through rows, columns
        check if coord is target,
        return true if target

        for quicker - use binary search
        """
        ## naive solution
        if matrix == []:
            return 0
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        return False
    
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

matrix2 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target2 = 13
solution = Solution()
print(solution.searchMatrix(matrix, target))
print(solution.searchMatrix(matrix2, target2))
