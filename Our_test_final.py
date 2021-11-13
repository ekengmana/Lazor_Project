import unittest


class unittest(unittest.Testcase):
    '''
        This is the unit tests to test whether functions and
        objects in this script are going well.

        **Returns**
            If there is anything wrong, msg shows a friendly message
    '''
    # In this sequence, we show
    # example_test[0] = the blocks types,
    # example_test[1] = block amounts
    # example_test[2] = the lazor start point and its direction,
    # example_test[3] = the points which lazor must pass
    # those becomes the setup environment for each .bff file
    Dark_1_test = (['B'], [3], [[(3, 0), (-1, 1)], [(1, 6), (1, -1)],[(3, 6), (-1, -1)], [(4, 3), (1, -1)]], [[0, 3], [6, 1]])
    Dark_1_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'x', 'x', 'o', 'x', 'o', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'o', 'x', 'B', 'x', 'o', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'B', 'x', 'B', 'x', 'x', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Mad_1_test = (['A', 'C'], [2, 1], [[(2, 7), (1, -1)]],
                  [[3, 0], [4, 3], [2, 5], [4, 7]])
    Mad_1_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'o', 'x', 'C', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'A', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'A', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Mad_4_test = (['A'], [5], [[(7, 2), (-1, 1)]], [[3, 4], [7, 4], [5, 8]])
    Mad_4_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'A', 'x', 'o', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'A', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'A', 'x', 'o', 'x', 'A', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                         ['x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x'],
                         ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Mad_7_test = (['A'], [6], [[(2, 1), (1, 1)], [(9, 4), (-1, 1)]],
                  [[6, 3], [6, 5], [6, 7], [2, 9], [9, 6]])
    Mad_7_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], [
        'x', 'A', 'x', 'o', 'x', 'A', 'x', 'o', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'o', 'x', 'o', 'x', 'A', 'x', 'o', 'x', 'o', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Numbered_6_test = (['A', 'B'], [3, 3], [
        [(4, 9), (-1, -1)], [(6, 9), (-1, -1)]], [[2, 5], [5, 0]])
    Numbered_6_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'B', 'x', 'o', 'x', 'o', 'x'],
                              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'A', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'B', 'x', 'o', 'x', 'A', 'x'],
                              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'A', 'x', 'x', 'x', 'o', 'x'],
                              ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                              ['x', 'B', 'x', 'o', 'x', 'o', 'x'],
                              ['x', 'x', 'x', 'x', 'x', 'x', 'x']]

    Showstopper_4_test = (['A', 'B'], [3, 3], [[(3, 6), (-1, -1)]], [[2, 3]])
    Showstopper_4_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'B', 'x', 'o', 'x', 'o', 'x'],
                                 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'A', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'B', 'x', 'o', 'x', 'A', 'x'],
                                 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'A', 'x', 'x', 'x', 'o', 'x'],
                                 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                                 ['x', 'B', 'x', 'o', 'x', 'o', 'x'],
                                 ['x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Tiny_5_test = (['A', 'C'], [3, 1], [[(4, 5), (-1, -1)]], [[1, 2], [6, 3]])
    Tiny_5_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'A', 'x', 'B', 'x', 'A', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'o', 'x', 'o', 'x', 'o', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
                          ['x', 'A', 'x', 'C', 'x', 'o', 'x'],
                          ['x', 'x', 'x', 'x', 'x', 'x', 'x']]
    Yarn_5_test = (['A'], [8], [[(4, 1), (1, 1)]], [[6, 9], [9, 2]])
    Yarn_5_solved_grid = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'o', 'x', 'B', 'x', 'x', 'x', 'o', 'x', 'o', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'o', 'x', 'A', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'A', 'x', 'x', 'x', 'o', 'x', 'o', 'x', 'A', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'o', 'x', 'x', 'x', 'A', 'x', 'o', 'x', 'x', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'A', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'A', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],['x', 'B', 'x', 'A', 'x', 'x', 'x', 'A', 'x', 'o', 'x'],['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

    # decide which test_example here we need
    if ".bff" in filename:
        filename = filename.split('.bff')[0]
    if filename == 'Dark_1.bff':
        example_test = Dark_1_test
        solved_grid = Dark_1_solved_grid
    if filename == 'Mad_1.bff':
        example_test = Mad_1_test
        solved_grid = Mad_1_solved_grid
    if filename == 'Mad_4.bff':
        example_test = Mad_4_test
        solved_grid = Mad_4_solved_grid
    if filename == 'Mad_7.bff':
        example_test = Mad_7_test
        solved_grid = Mad_7_solved_grid
    if filename == 'Numbered_6.bff':
        example_test = Numbered_6_test
        solved_grid = Numbered_6_solved_grid
    if filename == 'Showstopper_4.bff':
        example_test = Showstopper_4_test
        solved_grid = Showstopper_4_solved_grid
    if filename == 'Tiny_5.bff':
        example_test = Tiny_5_test
        solved_grid = Tiny_5_solved_grid
    if filename == 'Yarn_5.bff':
        example_test = Yarn_5_test
        solved_grid = Yarn_5_solved_grid

    # Get the result from the tested sample
    file = open_file(filename)
    # grid = identify_board(file)
    block_type, block_amount = identify_blocks(file)
    lazor_start = identify_lazor_start(file)
    lazor_points = identify_lazor_points(file)

    def Test_A(self):
        # Test 'Block' class by testing whether refractive block reflects laser
        self.assertEqual(example_test[0], block_type,
                         msg='Error: block type incorrect')

    def Test_B(self):
        self.assertEqual(example_test[1], block_amount,
                         msg='Error: block amount incorrect')

    def Test_C(self):
        self.assertEqual(
            example_test[2], lazor_start, msg='Error: No return correct laser')

    def Test_D(self):
        self.assertEqual(example_test[3], lazor_points,
                         msg='Error: wrong point is chosen')

    def Test_E(self):
        our_result_grid = save_grid
        self.assertEqual(solved_grid, our_result_grid,
                         msg='Error: no correct answer')


if __name__ == "__main__":
    unittest.main()
