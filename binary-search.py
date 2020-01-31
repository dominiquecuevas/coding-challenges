class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        LeetCode 74. Search a 2D Matrix
        get num of rows, cols
        floor divide by 2 to get coords of midpoint
        index into matrix with coords
        check if coord equal and return
        check if less than or greater than target
            update midpoint
            call recursively
        """
        if not matrix:
            return False
        
        for r in matrix:
            print(r)
        print("target:", target)
        print()
        row = len(matrix)
        column = len(matrix[0])
        left, right = 0, row * column - 1
        
        while left <= right: 
            print()
            print("left:", left)
            print("right:", right)

            mid = (left + right) // 2
            r = mid // column
            c = mid % column
            cur = matrix[r][c]
            print("mid:", mid)
            print("r:", r)
            print("c:", c)
            print("cur:", cur)
            if cur == target:
                print("found target")
                return True
            elif cur > target:
                print("cur > target, right = mid - 1")
                right = mid - 1
            else:
                print("cur < target, left = mid + 1")
                left = mid + 1
        return False


matrix = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10, 11]
]

matrix2 = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]


matrix3 = [
    [0, 1, 2],
    [3, 4, 5]
]

matrix4 = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

solution = Solution()
solution.searchMatrix(matrix2, 3)