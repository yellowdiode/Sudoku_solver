import copy
import random

small_grid_size = 3
grid_size = small_grid_size * small_grid_size
data = ['9,8,0', '9,0,8', '4,0,1', '1,2,0', '5,3,0', '6,1,5', '3,2,5', '4,2,7', '7,3,3', '2,3,8', '8,4,3', '3,4,7', '6,4,8', '9,5,4', '3,6,2', '2,6,3', '8,6,4', '7,7,2', '1,7,7', '4,8,2', '5,8,4', '2,8,7']


def solve(grid, pos_grids = None, stopper = None, exit = False):
    if pos_grids is None:
        pos_grids = []
    orig_pos_grids = list(pos_grids)
    least_pos = [0]*(grid_size+1)
    least_row = None
    least_column = None
    all_poss_num = [i+1 for i in range(grid_size)]
    if exit:
        return True
    for r in range(grid_size):
        square_r = int(r / small_grid_size) * small_grid_size
        for c in range(grid_size):
            square_c = int(c / small_grid_size) * small_grid_size

            if grid[r][c] is None:
                all_pos = list(all_poss_num)

                for i in range(grid_size):
                    if grid[r][i] in all_pos:
                        all_pos.remove(grid[r][i])
                    if grid[i][c] in all_pos:
                        all_pos.remove(grid[i][c])

                for row in range(small_grid_size):
                    for column in range(small_grid_size):
                        cur_square = grid[square_r + row][square_c + column]
                        if cur_square in all_pos:
                            all_pos.remove(cur_square)

                if len(all_pos) < len(least_pos):
                    least_pos = list(all_pos)
                    least_row = r
                    least_column = c

    if least_row is None:
        pos_grids.append(copy.deepcopy(grid))
        if stopper is not None:
            if len(pos_grids) >= stopper:
                exit = True
        return True

    if len(least_pos) == 0:
        return False

    for val in least_pos:
        grid[least_row][least_column] = val
        if solve(grid, pos_grids, stopper, exit):
            pass
        grid[least_row][least_column] = None
    if orig_pos_grids == pos_grids:
        return False
    return pos_grids


def print_grid(grid):
    print('-' * (2 * (grid_size + small_grid_size) + 1))
    for row in range(0, grid_size, small_grid_size):
        for r in range(row, row+small_grid_size):
            print('| ', end='')
            for column in range(0, grid_size, small_grid_size):
                for c in range(column, column+small_grid_size):
                    value = grid[-1 - r][c]
                    print('_' if value is None else value, '', end='')
                print('| ', end='')
            print()
        print('-'*(2*(grid_size+small_grid_size)+1))


def make_grid(values = []):
    grid = [[None] * grid_size for _ in range(grid_size)]
    for e in values:
        (v, r, c) = (int(i) for i in e.split(','))
        if not checker(grid, r, c, v):
            return None
        grid[r][c] = v
    return grid

def checker(grid, r, c, v):
    for i in range(grid_size):
        if grid[r][i] == v:
            return False
        if grid[i][c] == v:
            return False

    square_r = int(r / small_grid_size) * small_grid_size
    square_c = int(c / small_grid_size) * small_grid_size
    for row in range(small_grid_size):
        for column in range(small_grid_size):
            cur_square = grid[square_r + row][square_c + column]
            if cur_square == v:
                return False
    return True


def read_file(file_name):
    grid = []
    with open(file_name, "r") as f:
        for str in f:
            row = [None if s == '_' else int(s) for s in str.strip().split()]
            grid.insert(0, row)
    return grid


def generator():
    for i in range(0, 81):
        r = random.randint(0, grid_size-1)
        c = random.randint(0, grid_size-1)
        if grid[r][c] is None:
            place_holder = True
            while place_holder:
                v = random.randint(1, grid_size)
                if checker(grid, r, c, v):
                    grid[r][c] = v
                    pos_grids = solve(grid)
                    if len(pos_grids, None, 2) == 0:
                        pass
                    if len(pos_grids) == 1:
                        return True
                    place_holder = False
                    pass



    # grid = make_grid()
    # for r in range(grid_size):
    #     oh_no = False
    #     while not oh_no:
    #         for c in range(grid_size):
    #             all_pos_options = [i for i in range(1, 10)]
    #             checked = False
    #             while not checked:
    #
    #                 if len(all_pos_options) == 0:
    #                     oh_no = True
    #                     checked = True
    #                     pass
    #                 rand_val = random.choice(all_pos_options)
    #
    #                 if checker(grid, r, c, rand_val):
    #                     grid[r][c] = rand_val
    #                     pos_grids = solve(grid)
    #                     if len(pos_grids) == 1:
    #                         return pos_grids[0]
    #                     if len(pos_grids == 0):
    #                         all_pos_options.remove(rand_val)
    #                         grid[r][c] = None
    #                         pass
    #                     checked = True
    #                 else:
    #                     all_pos_options.remove(rand_val)
    #


# grid = read_file('grid')

def main():
    grid = make_grid(data)
    if grid:
        print_grid(grid)
        pos_grids = solve(grid)
        if len(pos_grids) > 0:
            num_pos_grids = len(pos_grids)
            grid = pos_grids[0]
            print_grid(grid)
            print(num_pos_grids)
        else:
            print("No solutions")
    else:
        print("some numbers overlap")


main()