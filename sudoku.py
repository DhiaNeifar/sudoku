import numpy as np

grid_1 = np.array([
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]).reshape(9, 9)


def display_grid(g):
    print('-----   displaying grid   -----\n')
    m, n = g.shape
    for i in range(m):
        line = ''
        if not i % 3 and i:
            print('-' * 31)
        for j in range(n):
            if not j % 3 and j:
                line += '|  '
                line += str(g[i, j])
                line += '  '
            else:
                line += str(g[i, j])
                line += '  '
        print(line)


def verify_row(row):
    r = row.copy()
    r.sort()
    for i in range(9):
        if r[0, i] != i + 1:
            return False
    return True


def verify_col(col):
    c = col.copy()
    c.sort()
    for i in range(9):
        if c[0, i] != i + 1:
            return False
    return True


def verify_small_grid(small_grid):
    flat = small_grid.reshape(1, 9)
    return verify_row(flat)


def verify_solved(grid):
    for i in range(3):
        for j in range(3):

            r = grid[i * 3 + j, :].reshape(1, 9)
            if not verify_row(r):
                return False

            c = grid[:, i * 3 + j].reshape(1, 9)
            if not verify_col(c):
                return False

            small_g = grid[i * 3: i * 3 + 3, j * 3: j * 3 + 3]
            if not verify_small_grid(small_g):
                return False

    return True


def possible(grid, x, y, n):
    for i in range(9):
        for elt in grid[x, :]:
            if elt == n:
                return False
        for elt in grid[:, y]:
            if elt == n:
                return False
        for elt in grid[x // 3 * 3: x // 3 * 3 + 3, y // 3 * 3: y // 3 * 3 + 3].reshape(9,):
            if elt == n:
                return False
    return True


def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[x, y] == 0:
                for n in range(1, 10):
                    if possible(grid, x, y, n):
                        grid[x, y] = n
                        solve(grid)
                        grid[x, y] = 0
                return
    print(grid)


def solve_sudoku(grid):
    if verify_solved(grid):
        return grid
    while not verify_solved(grid):
        for i in range(9):
            for j in range(9):
                if grid[i, j] == 0:
                    l = [i + 1 for i in range(9)]
                    for x in grid[i, :]:
                        if x in l:
                            l.remove(x)
                    for x in grid[:, j]:
                        if x in l:
                            l.remove(x)
                    for x in grid[i // 3 * 3: i // 3 * 3 + 3, j // 3 * 3: j // 3 * 3 + 3].reshape(9,):
                        if x in l:
                            l.remove(x)
                    if len(l) == 1:
                        grid[i, j] = l[0]

    return grid


if __name__ == '__main__':
    (solve(grid_1))
    print(solve_sudoku(grid_1))
