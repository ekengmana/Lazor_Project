import copy
import os
import time
from PIL import Image
from itertools import *
from sympy.utilities.iterables import multiset_permutations


class Block:
    '''
    This class is to define a bolck in the grid.
    There are four types of blocks, O or X
    or A(means reflex), B(means opaque), C(means reflect)
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
                        the current the location of the laser
        **result**
                True is not on the boundary and false if on the boundary
        '''
        if pos[0] <= 0 or pos[0] >= len_x - 1 or \
                pos[1] <= 0 or pos[1] >= len_y - 1:
            return False
        else:
            return True

    def laser(self, lasor_position, lasor_dir):
        '''
            This function is to update the position and direction of laser
            depending on the types of blocks which interact with the laser
            lasor_position refers to the coordinate of lasor in the grid
            lasor_dir refers to the driection of the laser.

            **parameters**
                    self:*object*
                    lasor_position:*tuple of 2 int*
                            The coordinates of lasor in the grid
                    lasor_dir:*tuple of 2 int*
                            The direction in which lasor is going.
                            Only 4 possible dirction(1,1),(1,-1),(-1,1),(-1,-1)

            Result: we can get new_direction from this function.
                    new_dirction is a list of new dirctions.
                    If block is 'B'absorbed, the list has 0 element
                    If block is 'A'reflected, the list has 1 element
                    If block is 'C'refracted, the list has 2 elements
            '''

        # Highlight:
        # The postion of laser is constitued by x and y
        # and either x or y is odd and the other is even.
        # if laser start point is (odd, odd) or (even, even),
        # then the lasor can never change dirction.

        # if the x of lasor point is odd
        if lasor_position[0] % 2 == 1:
            # if the block_type is reflect, the new direction is lasor_y * -1
            if self.type == 'A':
                new_direction = [lasor_dir[0], lasor_dir[1] * -1]
            # if the block_type is aborbed, then no new direction
            elif self.type == 'B':
                new_direction = []
            # if the block_type is refrated, then there are 2 new dirctions
            # new_dirction1 is the original direction
            # new_dirction2 is same as reflect direction
            else:
                new_direction1 = lasor_dir
                new_direction2 = (lasor_dir[0], lasor_dir[1] * -1)
                new_direction = [new_direction1, new_direction2]
        # if the x of lasor point is even (y is odd)
        if lasor_position[0] % 2 == 0:
            # if the block_type is reflect, the new direction is lasor_x * -1
            if self.type == 'A':
                new_direction = [(lasor_dir[0] * -1, lasor_dir[1])]
            elif self.type == 'B':
                new_direction = []
            else:
                new_direction1 = lasor_dir
                new_direction2 = [(lasor_dir[0] * -1, lasor_dir[1])]
                new_direction = [new_direction1, new_direction2]

        def laser_check(board, curr_pos, curr_dirc):
            '''
            This laser check function is to check whether laser
            interacts with a block and return the new direction of laser

            Guildlines:
            check the lasor position and if it hits a block,
            then change direction
            otherwise continue in the same direction

            **parameters**
            board:*list, list, string*
                    A list of list holds all elements on board
            curr_pos: *tuple of 2 int*
                    The current position of laser
            curr_dirc: *tuple of 2 int*
                    The current dirction of laser is going

            *result*
            new_dir: *list*
                    a list that hold new directions laser will be going
            '''

            x, y = curr_pos[0], curr_pos[1]
            new_dir = []
            # check upper and below position if x is odd
            if x % 2 == 1:
                # borad[x][y+curr_dirc[1]]means
                # the upper/lower position of the laser point
                # check whether this position is block
                # if this position is block, then change direction;
                # if not, new_dir stay the same
                if board[x][y + curr_dirc[1]] == 'A' or \
                        board[x][y + curr_dirc[1]] == 'B' or \
                        board[x][y + curr_dirc[1]] == 'C':
                    block = Block(
                        (x, y + curr_dirc[1]), board[x][y + curr_dirc[1]])
                    new_dir = block.laser(curr_pos, curr_dirc)
                else:
                    new_dir = copy.copy([curr_dirc])
            # check left and right of lasor position if x is even
            if x % 2 == 0:
                if board[x + curr_dirc[0]][y] == 'A' or \
                        board[x + curr_dirc[0]][y] == 'B' or \
                        board[x + curr_dirc[0]][y] == 'C':
                    block = Block(
                        (x + curr_dirc[0], y), board[x + curr_dirc[0][y]])
                    new_dir = block.laser(curr_pos, curr_dirc)
                else:
                    new_dir = copy.copy([curr_dirc])
            return new_dir
