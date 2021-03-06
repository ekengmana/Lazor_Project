import copy
import os
import time
from PIL import Image
from itertools import *
from sympy.utilities.iterables import multiset_permutations

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


def grid(grid, name="grid"):
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
    nBlock_x = len(grid)
    nBlock_y = len(grid[0])
    num_block_x = (nBlock_x - 1) / 2
    num_broader_x = (nBlock_x - 1) / 2 + 1
    dimx = num_block_x * BlockSize2 + num_broader_x * BlockSize1
    num_block_y = (nBlock_y - 1) / 2
    num_broader_y = (nBlock_y - 1) / 2 + 1
    dimy = num_block_y * BlockSize2 + num_broader_y * BlockSize1
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
                y = (jy / 2) * (BlockSize1 + BlockSize2)
                y_range = BlockSize1
                if jx % 2 == 0:  # (even, even)
                    x = (jx / 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize1
                else:  # (odd, even)
                    x = ((jx - 1) / 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize2
            else:  # (, odd)
                y = ((jy + 1) / 2) * (BlockSize1 + BlockSize2)
                y_range = BlockSize2
                if jx % 2 == 0:  # (even, odd)
                    x = (jx / 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize1
                else:  # (odd, odd)
                    x = ((jx + 1) / 2) * (BlockSize1 + BlockSize2)
                    x_range = BlockSize2
            # Assign color to the block
            for i in range(x_range):
                for j in range(y_range):
                    img.putpixel((x + i, y + j), colors[grid[jx][jy]])
    if not name.endswith(".png"):
        name += "_solution.png"
    img.save("%s" % name)


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

    def position_chk(board, pos):
        '''
        This function is to check whether a laser position is
        at the boundary of the board.

        **parameters**
                board: *list, list, string*
                        contains list of x and y coordinates
                        string represent the type of block on the board
                pos:*tuple*
                        the current the location of the lazor
        **result**
                True is not on the boundary and false if on the boundary
        '''
        if pos[0] <= 0 or pos[0] >= len_x - 1 or \
                pos[1] <= 0 or pos[1] >= len_y - 1:
            return False
        else:
            return True

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
                new_direction = [lazor_dir[0], lazor_dir[1] * -1]
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
        if lazor_position[0] % 2 == 0:
            # if the block_type is reflect, the new direction is lazor_x * -1
            if self.type == 'A':
                new_direction = [(lazor_dir[0] * -1, lazor_dir[1])]
            elif self.type == 'B':
                new_direction = []
            else:
                new_direction1 = lazor_dir
                new_direction2 = [(lazor_dir[0] * -1, lazor_dir[1])]
                new_direction = [new_direction1, new_direction2]

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

            x, y = curr_pos[0], curr_pos[1]
            new_dir = []
            # check upper and below position if x is odd
            if x % 2 == 1:
                # borad[x][y+curr_dirc[1]]means
                # the upper/lower position of the lazor point
                # check whether this position is block
                # if this position is block, then change direction;
                # if not, new_dir stay the same
                if board[x][y + curr_dirc[1]] == 'A' or \
                        board[x][y + curr_dirc[1]] == 'B' or \
                        board[x][y + curr_dirc[1]] == 'C':
                    block = Block(
                        (x, y + curr_dirc[1]), board[x][y + curr_dirc[1]])
                    new_dir = block.lazor(curr_pos, curr_dirc)
                else:
                    new_dir = copy.copy([curr_dirc])
            # check left and right of lazor position if x is even
            if x % 2 == 0:
                if board[x + curr_dirc[0]][y] == 'A' or \
                        board[x + curr_dirc[0]][y] == 'B' or \
                        board[x + curr_dirc[0]][y] == 'C':
                    block = Block(
                        (x + curr_dirc[0], y), board[x + curr_dirc[0][y]])
                    new_dir = block.lazor(curr_pos, curr_dirc)
                else:
                    new_dir = copy.copy([curr_dirc])
            return new_dir
