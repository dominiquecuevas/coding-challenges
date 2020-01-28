class Solution:
    """
    loop through rows, then columns
    check if element is equal to 1
        do dfs search recursively with helper function
        each search counts 1 for island
        base case - check if reached last coord
            row == rows, col == cols
        base case - check if all surrounding are 0's
    """
    def numIslands(self, grid):
        # num of rows, num of columns
        row, col = len(grid), len(grid[0])
        islands = 0
        # coordinates
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    print()
                    print("on i:", i)
                    print("on j:", j)
                    dfs(grid, row, col, i, j)
                    islands += 1
        return islands

def dfs(grid, row, col, x, y):
    print
    print("on x:", x)
    print("on y:", y)
    for r in grid:
        print(r)

    if grid[x][y] == 0:
        print("grid[x][y] == 0 /return")
        return
    grid[x][y] = 0

    if x != 0:  # check if not zenith row, to go north
        print("x != 0 /going x-1")
        print("x-1:", x-1)
        print("y:", y)
        dfs(grid, row, col, x-1, y)
    if x != row - 1:  # check if not on last row, to go south
        print("x != row-1 /going x+1")
        print("x+1:", x+1)
        print("y:", y)
        dfs(grid, row, col, x+1, y)
    if y != 0:  # check if not zenith column, to go west
        print("y !=0 /going y-1")
        print("x:", x)
        print("y-1:", y-1)
        dfs(grid, row, col, x, y-1)
    if y != col - 1:  # check if not last column, to go east
        print("y != col - 1 /going y+1")
        print("x:", x)
        print("y+1:", y+1)
        dfs(grid, row, col, x, y+1)

solution = Solution()
grid = [
        [1,1,1,1,0],
        [1,0,1,1,0],
        [0,0,0,0,0]
        ]
grid2 = [
        [1,1,1,1,0],
        [1,0,1,1,0],
        [0,1,0,0,0]
        ]

grid3 = [
        [1,0,1],
        [0,1,0]
]

print(solution.numIslands(grid3))