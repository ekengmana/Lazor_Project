# This file takes in a .bff file and reads it out
# Functions will be to read it in, split it by line
# then split the parts into the grid, block types/amounts
# lazor origins/angles, and lazor points to cross

# Credit to Kuan-Lin and his group. Their former project was found on github at
# https://github.com/charliecharlie29/SoftwareCarpentryLazorProject
# and the files acted as a guide to help us.

import copy
import math
import time
from PIL import Image, ImageDraw
from sympy.utilities.iterables import multiset_permutations

lazor_path = []


def get_colors():
    '''
    In this function, we are going to color the map by using the RBG number.
    The result will be returned to the RBG of each kind of block.
    Credit: this function is modified with get_color function
    in maze generation code in weekly challenge7.
    '''
    return {
        'x': (20, 20, 20),
        'A': (0, 0, 160),
        'o': (50, 50, 50),
        'B': (130, 0, 0),
        'C': (0, 150, 150), }
    # 'L': (0, 255, 255)}


def save_grid(grid, targets, origins, lazor_pos_list, path, name="grid"):
    '''
    This fucntion is to save a grid to a file.
    Credit: This function is modified from save_maze function
    in weekly challenge7.
    **parameters**
        grid: *list, list, str*
            A list of lists, holding strings specifing the different aspects.
        name:*str, optional*
            The name of the grid.png file to save.
    '''
    # BlockSize is the amount of pixels of
    # each broader(BlockSize1) or block(BlockSize2)
    BlockSize1 = 5
    BlockSize2 = 30
    circle_size = 10
    nBlock_x = len(grid)
    nBlock_y = len(grid[0])
    num_block_x = (nBlock_x - 1) / 2
    num_broader_x = (nBlock_x - 1) / 2 + 1
    dimx = int(num_block_x * BlockSize2 + num_broader_x * BlockSize1)
    # print(dimx)
    num_block_y = (nBlock_y - 1) / 2
    num_broader_y = (nBlock_y - 1) / 2 + 1
    dimy = int(num_block_y * BlockSize2 + num_broader_y * BlockSize1)
    # print(dimy)
    colors = get_colors()

    # Verify that all values in the grid are valid colors.
    ERR_MSG = "Error, invalid grid value found!"
    assert all([x in colors.keys() for row in grid for x in row]), ERR_MSG

    img = Image.new("RGB", (dimx, dimy), color=0)

    # Parse "grid" into pixels
    # The broader area is thin line while the block area is a block.
    # Then assign the color of each areas using putpixel
    for jy in range(nBlock_y):  # jy is y corrodinate of grid, similar with jx.
        for jx in range(nBlock_x):
            if jy % 2 == 0:  # jy is even
                y = (jy // 2) * (BlockSize1 + BlockSize2)
                y_range = BlockSize1
                if jx % 2 == 0:  # (even, even)
                    x = (jx // 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize1
                else:  # (odd, even)
                    x = ((jx + 1) // 2) * \
                        (BlockSize1 + BlockSize2) - BlockSize2
                    x_range = BlockSize2

            else:  # (, odd)
                y = ((jy + 1) // 2) * (BlockSize1 + BlockSize2) - BlockSize2
                y_range = BlockSize2
                if jx % 2 == 0:  # (even, odd)
                    x = (jx // 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize1
                else:  # (odd, odd)
                    x = ((jx + 1) // 2) * \
                        (BlockSize1 + BlockSize2) - BlockSize2
                    x_range = BlockSize2
            # Assign color to the block
            # print(x_range, y_range)
            for i in range(x_range):
                for j in range(y_range):
                    # print(i, j)
                    img.putpixel((x + i, y + j), colors[grid[jx][jy]])
    draw = ImageDraw.Draw(img)
    # creates a copy that draws over the image to mark
    # lazor targets and the lazors.

    for i in range(len(origins)):
        # draw the origin points of lazors
        draw.ellipse((int((origins[i][0][0] * (BlockSize1 + BlockSize2) / 2)),
                      int((origins[i][0][1] * (BlockSize1 + BlockSize2) / 2)),
                      int((origins[i][0][0] * (BlockSize1 + BlockSize2) /
                           2) - (circle_size / 2) + circle_size),
                      int((origins[i][0][1] * (BlockSize1 + BlockSize2) / 2) -
                          (circle_size / 2) + circle_size)), fill=(255, 25, 25))
    # lazor_pos_list = lazor_go(grid, origins, targets)
    # print(lazor_pos_list[0][1][0])
    # print(origins[0][0])
    # print([origins[0][0],lazor_pos_list[0][1][0]])
    # print(lazor_pos_list[0][1][0][0]+1)
    # print(lazor_pos_list)

    for i in range(len(lazor_pos_list)):
        # print(lazor_pos_list[i])
        for j in range(len(lazor_pos_list[i]) - 2):
            # draw the path of the lazor(s) in the board
            x1 = lazor_pos_list[i][j][0][0] * \
                (BlockSize1 + BlockSize2) / 2 + circle_size / 4
            y1 = lazor_pos_list[i][j][0][1] * \
                (BlockSize1 + BlockSize2) / 2 + circle_size / 4
            x2 = lazor_pos_list[i][j + 1][0][0] * \
                (BlockSize1 + BlockSize2) / 2 + circle_size / 4
            y2 = lazor_pos_list[i][j + 1][0][1] * \
                (BlockSize1 + BlockSize2) / 2 + circle_size / 4
            # print(x1,y1,x2,y2)
            draw.line([(x1, y1), (x2, y2)], fill=(255, 0, 0), width=2)

    # print(path[0], path[1])
    print(path)
    # print(path[0][0],path[0][0][1],path[1][0], path[1][0][0])

    for i in range(len(path) - 1):
        x1 = path[i][0][0] * \
            (BlockSize1 + BlockSize2) / 2 + circle_size / 4
        y1 = path[i][0][1] * \
            (BlockSize1 + BlockSize2) / 2 + circle_size / 4
        x2 = path[i + 1][0][0] * \
            (BlockSize1 + BlockSize2) / 2 + circle_size / 4
        y2 = path[i + 1][0][1] * \
            (BlockSize1 + BlockSize2) / 2 + circle_size / 4
        print(x1, y1, x2, y2)
        draw.line([(x1, y1), (x2, y2)], fill=(255, 0, 0), width=2)

    for i in range(len(targets)):
        # draw the lazor targets for the lazor to pass through
        draw.ellipse((int((targets[i][0] * (BlockSize1 + BlockSize2) / 2)),
                      int((targets[i][1] * (BlockSize1 + BlockSize2) / 2)),
                      int((targets[i][0] * (BlockSize1 + BlockSize2) / 2) -
                          (circle_size / 2) + circle_size),
                      int((targets[i][1] * (BlockSize1 + BlockSize2) / 2) -
                          (circle_size / 2) + circle_size)), fill=(125, 255, 25))
    if not name.endswith(".png"):
        name += "_solution.png"
    img.save("%s" % name)
    # for i in range(len(targets)):
    #     cv2.circle(new_img, (int((targets[i][0] * (BlockSize1 + BlockSize2) / 2) + (circle_size / 2)),
    #         int((targets[i][1] * (BlockSize1 + BlockSize2) / 2) + (circle_size / 2))), 5, (0, 255, 0), -1)
    # cv2.imwrite(new_img)


def position_chk(board, pos):
    '''
    This function is to check whether a laser position is
    at the boundary of the board.
    **parameters**
            board: *list, list, string*
                    contains strings of spaces or invalid spots or blocks
                    on the board
                    string represent the type of block on the board
            pos: *tuple*
                    the current the location of the lazor
    **result**
            True is not in the boundary and false if in the boundary
    '''

    if pos[0] <= 0 or pos[0] >= len(board) - 1 or \
            pos[1] <= 0 or pos[1] >= len(board[0]) - 1:
        return False
    else:
        return True


class Block:
    '''
    This class is to define a bolck in the grid.
    There are four types of blocks, O or X
    or A(means reflect), B(means opaque), C(means refract)
    '''

    def __init__(self, block_positions, type):
        '''
        In this function, the class of blocks is initialized
        block_positions contains x and y coordinates.
        **parameters**
                block_positions: *tuple, int*
                        the x and y corrdinates
                        of blocks on board as a tunple of int
                type: *string*
                        The type of the block
        '''
        self.positions = block_positions
        self.type = type

    def lazor(self, lazor_position, lazor_dir):
        '''
            This function is to update the position and direction of lazor
            depending on the types of blocks which interact with the lazor
            lazor_position refers to the coordinate of lazor in the grid
            lazor_dir refers to the driection of the lazor.
            **parameters**
                    self:*object*
                    lazor_position:*tuple of 2 int*
                            The coordinates of lazor in the grid
                    lazor_dir:*tuple of 2 int*
                            The direction in which lazor is going.
                            Only 4 possible dirction(1,1),(1,-1),(-1,1),(-1,-1)
            Result: we can get new_direction from this function.
                    new_dirction is a list of new dirctions.
                    If block is 'B'absorbed, the list has 0 element
                    If block is 'A'reflected, the list has 1 element
                    If block is 'C'refracted, the list has 2 elements
            '''

        # Highlight:
        # The postion of lazor is constitued by x and y
        # and either x or y is odd and the other is even.
        # if lazor start point is (odd, odd) or (even, even),
        # then the lazor can never change dirction.

        # if the x of lazor point is odd
        if lazor_position[0] % 2 == 1:
            # if the block_type is reflect, the new direction is lazor_y * -1
            if self.type == 'A':
                new_direction = [(lazor_dir[0], lazor_dir[1] * -1)]
            # if the block_type is aborbed, then no new direction
            elif self.type == 'B':
                new_direction = []
            # if the block_type is refrated, then there are 2 new dirctions
            # new_dirction1 is the original direction
            # new_dirction2 is same as reflect direction
            else:
                new_direction1 = lazor_dir
                new_direction2 = (lazor_dir[0], lazor_dir[1] * -1)
                new_direction = [new_direction1, new_direction2]
        # if the x of lazor point is even (y is odd)
        else:
            # if the block_type is reflect, the new direction is lazor_x * -1
            if self.type == 'A':
                new_direction = [(lazor_dir[0] * -1, lazor_dir[1])]
            elif self.type == 'B':
                new_direction = []
            else:
                new_direction1 = lazor_dir
                new_direction2 = (lazor_dir[0] * -1, lazor_dir[1])
                new_direction = [new_direction1, new_direction2]
        return new_direction


def lazor_check(board, curr_pos, curr_dirc):
    '''
    This lazor check function is to check whether lazor
    interacts with a block and return the new direction of lazor
    Guildlines:
    check the lazor position and if it hits a block,
    then change direction
    otherwise continue in the same direction
    **parameters**
    board:*list, list, string*
            A list of list holds all elements on board
    curr_pos: *tuple of 2 int*
            The current position of lazor
    curr_dirc: *tuple of 2 int*
            The current dirction of lazor is going
    *result*
    new_dir: *list*
            a list that hold new directions lazor will be going
    '''

    # print(curr)
    x, y = curr_pos[0], curr_pos[1]
    new_dir = []
    # check upper and below position if x is odd
    if x % 2 == 1:
        # board[x][y+curr_dirc[1]]means
        # the upper/lower position of the lazor point
        # check whether this position is block
        # if this position is block, then change direction;
        # if not, new_dir stay the same
        if (board[x][y + curr_dirc[1]] == 'A') or \
                (board[x][y + curr_dirc[1]] == 'B') or \
                (board[x][y + curr_dirc[1]] == 'C'):
            block = Block(
                (x, y + curr_dirc[1]), board[x][y + curr_dirc[1]])
            new_dir = block.lazor(curr_pos, curr_dirc)
            # print(new_dir)
        else:
            new_dir = copy.deepcopy([curr_dirc])
            # print(new_dir)
    # check left and right of lazor position if x is even
    else:
        if board[x + curr_dirc[0]][y] == 'A' or \
                board[x + curr_dirc[0]][y] == 'B' or \
                board[x + curr_dirc[0]][y] == 'C':
            block = Block(
                (x + curr_dirc[0], y), board[x + curr_dirc[0]][y])
            new_dir = block.lazor(curr_pos, curr_dirc)
            # print(new_dir)
        else:
            new_dir = copy.deepcopy([curr_dirc])
            # print(new_dir)
    return new_dir


def lazor_go(board, lazor_origin, target_position):
    '''
    Organize the board, and get the lazors running from
    a start position tothe end position.
    During this period, every lazor's position will be checked
    to make sure it goes through the certain target spot.
    **Parameters**
        board: *list, list, string*
            Where those spot located, which will show as the form of a list
            indicating the type of those blocks
        lazor_origin: *list, list, tuple, int*
            Those lists shows the lazor's starting position.
            And the other list is the lazor's original position
        target_position: *list, tuple, int*
            The intersections position where the lazor meet with those wall
    **Returns**
        *boolean*
            The judgment statement of whether the lazor are intersected with
            all the target position. If all target position get meet, then
            they get the True as a feedback.
    '''

    n = 0
    max_n = 1000

    lazor_pos_list = []
    path2 = []
    target_pool = copy.deepcopy(target_position)
    for curr_pos in lazor_origin:
        lazor_pos_list.append([curr_pos])

    all_meet = False

    while not all_meet:
        n = n + 1
        for i in range(len(lazor_pos_list)):
            # print(len(lazor_pos_list))
            if len(lazor_pos_list[i][-1]) == 0:
                # last position in lazor is empty
                continue
            curr_pos, curr_dirc = lazor_pos_list[i][-1][0], lazor_pos_list[i][-1][1]
            # gives current position of lazor and its current direction
            # print(curr_pos)
            # print(curr_dirc)

            if (not position_chk(board, curr_pos)) and (n > 1):
                # check if lazor is at the edge of the board
                # go to the next lazor present if there is one
                lazor_pos_list[i].append([])
                continue

            next_dir = lazor_check(board, curr_pos, curr_dirc)
            # moves the lazor further in current direction
            # print(next_dir)
            if len(next_dir) == 1:
                # block was a reflect block
                curr_dirc = next_dir[0]
                curr_pos = tuple(map(sum, zip(curr_pos, curr_dirc)))
                lazor_pos_list[i].append([curr_pos, curr_dirc])

            elif len(next_dir) == 2:
                # a refract block was in the way, so 2 lazors are now present
                dir_one, dir_two = next_dir[0], next_dir[1]
                # print(dir_one)
                pos_one = tuple(map(sum, zip(curr_pos, dir_one)))
                pos_two = tuple(map(sum, zip(curr_pos, dir_two)))
                # print(pos_one, pos_two)
                lazor_pos_list[i].append([pos_one, dir_one])
                lazor_pos_list.append([[pos_two, dir_two]])
                path2 = [[curr_pos]]
                path2.append([pos_two])

            else:
                lazor_pos_list[i].append([])

        # See if all the target position come to list
        lazor_in_list = 0
        for lazor_i in lazor_pos_list:
            if len(lazor_i[-1]) != 0:
                lazor_in_list = lazor_in_list + 1

        if lazor_in_list == 0 or n == max_n:
            break
    # print(path2)
    for lazor_i in lazor_pos_list:
        for positions in lazor_i:
            try:
                if (positions[0] in target_pool):
                    # print(target_pool)
                    target_pool.remove(positions[0])
            except IndexError:
                pass

    if len(target_pool) == 0:
        return True, lazor_pos_list, path2
    else:
        return False, lazor_pos_list, path2


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
                lazor.append([(int(line[2]), int(line[4])),
                              (-1 * int(line[7]), -1 * int(line[10]))])
            elif line[6] == '-':
                # account for formatting of - symbols
                lazor.append([(int(line[2]), int(line[4])),
                              (-1 * int(line[7]), int(line[9]))])
                # angle.append((-1 * int(line[7]), int(line[9])))
            elif line[8] == '-':
                # account for formatting of - symbols
                lazor.append([(int(line[2]), int(line[4])),
                              (int(line[6]), -1 * int(line[9]))])
                # angle.append((int(line[6]), -1 * int(line[9])))
            else:
                lazor.append([(int(line[2]), int(line[4])),
                              (int(line[6]), int(line[8]))])
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
    # print(format_grid)
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
    # print(grid)
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


def solver(fptr):
    '''
    Solves a lazor .bff file using sympy
    **Parameters**
        fptr: *str*
            name of a file to open, read, and solve
    **Returns**
        solved: *boolean*
            whether the puzzle is solved
    '''
    if '.bff' in fptr:
        filename = fptr.split('.bff')[0]
    file = open_file(fptr)
    grid = identify_board(file)
    block_type, block_amount = identify_blocks(file)
    lazor_start = identify_lazor_start(file)
    lazor_points = identify_lazor_points(file)
    # create a copy of the grid that can be worked with
    spaces_open = []
    for y in grid:
        for x in y:
            if x == 'o':
                spaces_open.append(x)
                # take in all of the available spaces that can be used to place blocks
                # in a grid for the upcoming permutation methods
    tracker = 0
    for i in range(len(block_type)):
        count = 0
        if block_type[i] == 'A':
            for j in range(tracker, tracker + block_amount[i]):
                spaces_open[tracker + count] = 'A'
                count += 1
            tracker = tracker + count
        elif block_type[i] == 'B':
            for j in range(tracker, tracker + block_amount[i]):
                spaces_open[tracker + count] = 'B'
                count += 1
            tracker = tracker + count
        elif block_type[i] == 'C':
            for j in range(tracker, tracker + block_amount[i]):
                spaces_open[tracker + count] = 'C'
                count += 1
            tracker = tracker + count
    # print(spaces_open)
    permutations = list(multiset_permutations(spaces_open))
    length = len(grid)
    width = len(grid[0])
    Solution = False

    for possible_solution in permutations:
        possible_grid = copy.deepcopy(grid)
        for l in range(length):
            for w in range(width):
                if possible_grid[l][w] == 'o':
                    possible_grid[l][w] = possible_solution.pop(0)
        result, lazor_pos_list, path2 = lazor_go(
            possible_grid, lazor_start, lazor_points)
        if result == True:
            # print(path)
            print("The solution is founded")
            save_grid(possible_grid, lazor_points, lazor_start,
                      lazor_pos_list, path2, name="%s_solution.png" % filename)
            Solution = True
            break
    if not Solution:
        print("No solution for it!")
        # save_grid(possible_grid, name="%s_solution.png" % filename)


if __name__ == '__main__':
    start = time.time()
    solver('mad_1.bff')
    solver('mad_4.bff')
    solver('mad_7.bff')
    solver('numbered_6.bff')
    solver('showstopper_4.bff')
    solver('tiny_5.bff')
    solver('yarn_5.bff')
    solver('dark_1.bff')
    end = time.time()
    print('solving all puzzles took %f seconds' % (end - start))
