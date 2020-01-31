def get_island_count(matrix):
    islands = 0
    row, col = len(matrix), len(matrix[0])

    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 1:
                dfs(matrix, row, col, r, c)
                islands +=1
    return islands

def dfs(matrix, row, col, r, c):
    if matrix[r][c] == 0:
        return
    matrix[r][c] = 0
    if r != 0:
        dfs(matrix, row, col, r-1, c)
    if r != row-1:
        dfs(matrix, row, col, r+1, c)
    if c != 0:
        dfs(matrix, row, col, r, c-1)
    if c != col-1:
        dfs(matrix, row, col, r, c+1)

matrix = [
            [0, 1, 0],
            [1, 0, 1]
]