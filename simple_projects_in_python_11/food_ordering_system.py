import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]
        ]

def possible(row, column, number):
    global grid

    # Is the number appearing in the given row?
    for num in range(0, 9):
        if grid[row][num] == number:
            return False
        
    # Is the number appearing in the given column?
    for num in range(0, 9):
        if grid[num][column] == number:
            return False

    # Is the number appearing in the given square?
    column_x = (column // 3) * 3
    row_y = (row // 3) * 3

    for row_num in range(0, 3):
        for column_num in range(0, 3):
            if grid[row_y + row_num][column_x + column_num] == number:
                return False
            
    return True

def solve():
    global grid

    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] - 0

                return
            
    print(np.matrix(grid))
    input("More possible solutions")

solve()