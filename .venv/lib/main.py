small_grid_size = 3
grid_size = small_grid_size * small_grid_size
data = ['8,0,0', '3,1,2', '6,1,3', '7,2,1', '9,2,4', '2,2,6', '5,3,1', '7,3,5', '4,4,4', '5,4,5', '7,4,6', '1,5,3', '3,5,7', '1,6,2', '6,6,7', '8,6,8', '8,7,2', '5,7,3', '1,7,7', '9,8,1', '4,8,6']


def solve(grid):
    least_pos = [0]*(grid_size+1)
    least_row = None
    least_column = None
    all_poss_num = [i+1 for i in range(grid_size)]

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
                    least_pos = all_pos
                    least_row = r
                    least_column = c

    if len(least_pos) > grid_size:
        return True

    if len(least_pos) == 0:
        return False

    for val in least_pos:
        grid[least_row][least_column] = val
        answer = solve(grid)
        if answer:
            return answer
    grid[least_row][least_column] = None
    return False


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



# grid = read_file('grid')

def main():
    grid = make_grid(data)
    print_grid(grid)
    if grid:
        if solve(grid):
            print_grid(grid)
        else:
            print("No solutions")

main()