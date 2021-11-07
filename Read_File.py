# This file takes in a .bff file and reads it out
# Functions will be to read it in, split it by line
# then split the parts into the grid, block types/amounts
# lazor origins/angles, and lazor points to cross

### Credit to Kuan-Lin and his group. Their former project was found on github at 
### https://github.com/charliecharlie29/SoftwareCarpentryLazorProject
### and the files acted as a guide to help us.

def split_by_line(fptr):
    '''
    A function to split a .bff file into separate lines
    **Parameters**
        fptr: *io.TextIOWrapper*
            A file with text inside that will be read for the lazor game
    
    **Returns**
        split_fptr: *list, str*
            A list of various strings, each representing a line from fptr

    '''
    split_fptr = []
    x = str(fptr.readline())
    for line in fptr:
        # create a list containing each line
        # print(x)
        # print(fptr)
        x = str(line)
        x.split('\n')
        x = x.strip("['").strip("']").strip(",")
        # print(x)
        if x[0][0] == '#' or x[0][0] == ' ' or x[0][0] == '\n':
            # omits unnecessary information
            # speed up parsing
            continue
        else:
            split_fptr.append(x)
    return split_fptr

def identify_blocks(fptr_lines):
    '''
    Identifies the blocks available to use in a puzzle
    **Parameters**
        fptr_lines: *list, str*
            a list of different strings from the .bff file
    **Returns**
        block_type: *list, str*
            a list of strings correspoding to the block types 'A', 'B', and 'C'
        block_amount: *list, int*
            a list of integers corresponding to the amount of a block type
            using a corresponding index number of block_type
    '''

    block_type = []
    block_amount = []
    # print(start_line)
    for i in range(len(fptr_lines)):
        line = fptr_lines[i]
        if 'L' in fptr_lines[i]:
            # reached the end of blocks listed
            break
        elif (line[0] == 'A' or line[0] == 'B' or line[0] == 'C') and 'o' not in line:
            # accounts for letters in "GRID START"
            # the 'and' prevents an error with 'yarn_5.bff
            block_type.append(line[0])
            # block types in index
            block_amount.append(int(line[2]))
            # block amounts in corresponding index of block type
    return block_type, block_amount
    


def identify_lazor_start(fptr_lines):
    '''
    Identifies the start position and angle of lazors in the puzzle.
    **Parameters**
        fptr_lines: *list, str*
            a list of different strings from the .bff file
    **Returns**
        lazor: *list, list, tuple, int*
            a list containing a list of coordinates where each list is a lazor starting position
            and angle
    '''

    lazor = list()
    for i in range(len(fptr_lines)):
        line = fptr_lines[i]
        if line[0] == 'P':
            # all lazors have been identified
            break
        elif 'L' in fptr_lines[i]:
            # print(fptr_lines[i])
            line = (fptr_lines[i])
            if line[6] == '-' and line[9] == '-':
                # account for formatting of - symbols
                lazor.append([(int(line[2]), int(line[4])), (-1 * int(line[7]), -1 * int(line[10]))])
            elif line[6] == '-':
                # account for formatting of - symbols
                lazor.append([(int(line[2]), int(line[4])), (-1 * int(line[7]), int(line[9]))])
                # angle.append((-1 * int(line[7]), int(line[9])))
            elif line[8] == '-':
                # account for formatting of - symbols
                lazor.append([(int(line[2]), int(line[4])), (int(line[6]), -1 * int(line[9]))])
                # angle.append((int(line[6]), -1 * int(line[9])))
            else:
                lazor.append([(int(line[2]), int(line[4])), (int(line[6]), int(line[8]))])
                # angle.append((int(line[6]), int(line[8])))
            # lazor.append
    return lazor


def identify_lazor_points(fptr_lines):
    '''
    **Parameters**
        fptr_lines: *list, str*
            a list of different strings from the .bff file
    **Returns**
        lazor_point: *list, tuple, int*
            a list of coordinates where each list index is a point on the grid
            that must be crossed by the lazor in the board.
    '''

    lazor_point = []
    for i in range(len(fptr_lines)):
        # parse through the list
        # identify the list of lazor points
        if 'P ' in fptr_lines[i]:
            # indicates a point to cross
            line = str(fptr_lines[i])
            lazor_point.append((int(line[2]), int(line[4])))
            # add the coordinates to the list
    return lazor_point


def create_grid(grid):
    '''
    Use the lines in grid to create a board
    **Parameters**
        grid: *list, str*
            a list of strings containing information about the board
    **Returns**
        format_grid: *list, list, str*
            a new grid simplified to only contain 
            'x', 'o', 'A', 'B', and 'C'.
            spacings between them are just 's'
    '''
    format_grid = list()
    # print(type(grid))
    count = 0
    for line in grid:
        # print(line)
        # grid.append(' ')
        new_grid = []
        for letter in range(len(line)):
            # print(len(line))
            # print(line[letter])
            if line[letter] == ' ':
                continue
            elif line[letter] == 'o':
                new_grid.append(line[letter])
            elif line[letter] == 'x':
                new_grid.append(line[letter])
            elif line[letter] == 'A':
                new_grid.append(line[letter])
            elif line[letter] == 'B':
                new_grid.append(line[letter])
            elif line[letter] == 'C':
                new_grid.append(line[letter])
        format_grid.append(new_grid)
        # create a grid with the information from the .bff file
        count += 1
    print(format_grid)
    gridx = 2 * len(format_grid) + 1
    gridy = 2 * len(format_grid[0]) + 1
    # obtain the length and width of the actual grid
    format_grid_2 = [['x' for x in range(gridx)] for y in range(gridy)]
    # a reformatted grid to include the spaces not available for blocks
    # place 'x' in every spot
    for i in range(0, len(format_grid)):
        for j in range(0, len(format_grid[0])):
            format_grid_2[2 * j + 1][2 * i + 1] = format_grid[i][j]
            # for every 2 blocks, place the information of the original
            # formatted grid to create a full grid, replacing certain 'x'
    # print(format_grid)
    return format_grid_2


def identify_board(fptr_lines):
    '''
    Identifies the grid size and returns a grid with the corresponding size
    **Parameters**
        fptr_lines: *list, str*
            a list of different strings from the .bff file
    **Returns**
        grid: *list, list, str*
            the size of the grid in the .bff file and the corresponding spaces
            in the array, 'o', 'x', 'A', 'B', 'C', and 's'
            the x grid length is the length of each list of list
            the y grid length is the number of lists * 2 + 1
    '''

    grid = []
    # print(column)
    for i in range(len(fptr_lines)):
        # parse through the list
        # print(fptr_lines[i])
        if 'GRID STOP' in fptr_lines[i]:
            # no need to continue since grid is already identified
            break
        elif 'GRID START' in fptr_lines[i]:
            # identifies the start of the grid
            # fptr_lines.remove(fptr_lines[i])
            continue
        line = str(fptr_lines[i])
        # print(line)
        grid.append(line)
    # print(grid)
    grid = create_grid(grid)
    return grid
            
def open_file(name):
    '''
    Opens a .bff file and creates a new list of strings from it
    to be used for other functions
    **Parameters**
        name: *str*
            name of a file
    **Returns**
        fptr_lines: *list, str*
            a list of strings separated by lines for identifying 
            different parts of the files
    '''
    fptr = open(name, 'r')
    # open the file in read mode
    fptr_lines = split_by_line(fptr)
    # create a list of strings of the file's components
    return fptr_lines


if __name__ == '__main__':
    fptr_lines = open_file('mad_7.bff')
    # print(fptr_lines)
    grid = identify_board(fptr_lines)
    # print(grid)
    # print(line_count1)
    block_type, block_amount = identify_blocks(fptr_lines)
    lazor_start = identify_lazor_start(fptr_lines)
    lazor_points = identify_lazor_points(fptr_lines)
    print(grid)
    print(block_type)
    print(block_amount)
    print(lazor_start)
    # print(angle)
    print(lazor_points)
    
