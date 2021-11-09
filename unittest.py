import unittest


class Lazor_Unit_Test(unittest.TestCase):
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
    Dark_1_test = (['B'], [3], [[(3, 0), (-1, 1)], [(1, 6), (1, -1)],
                                [(3, 6), (-1, -1)], [(4, 3), (1, -1)]], [[0, 3], [6, 1]])
    Mad_1_test = (['A', 'C'], [2, 1], [[(2, 7), (1, -1)]],
                  [[3, 0], [4, 3], [2, 5], [4, 7]])
    Mad_4_test = (['A'], [5], [[(7, 2), (-1, 1)]], [[3, 4], [7, 4], [5, 8]])
    Mad_7_test = (['A'], [6], [[(2, 1), (1, 1)], [(9, 4), (-1, 1)]],
                  [[6, 3], [6, 5], [6, 7], [2, 9], [9, 6]])
    Numbered_6_test = (['A', 'B'], [3, 3], [
        [(4, 9), (-1, -1)], [(6, 9), (-1, -1)]], [[2, 5], [5, 0]])
    Showstopper_4.test = (['A', 'B'], [3, 3], [[(3, 6), (-1, -1)]], [[2, 3]])
    Tiny_5.test = (['A', 'C'], [3, 1], [[(4, 5), (-1, -1)]], [[1, 2], [6, 3]])
    Yarn_5.test = (['A'], [8], [[(4, 1), (1, 1)]], [[6, 9], [9, 2]])

    def unit_test(filename):
        # decide which test_example here we need
        if ".bff" in filename:
            filename = filename.split('.bff')[0]
        if filename == 'Dark_1.bff':
            example_test = Dark_1_test
        if filename == 'Mad_1.bff':
            example_test = Mad_1_test
        if filename == 'Mad_4.bff':
            example_test = Mad_4_test
        if filename == 'Mad_7.bff':
            example_test = Mad_7_test
        if filename == 'Numbered_6.bff':
            example_test = Numbered_6_test
        if filename == 'Showstopper_4.bff':
            example_test = Showstopper_4_test
        if filename == 'Tiny_5.bff':
            example_test = Tiny_5_test
        if filename == 'Yarn_5.bff':
            example_test = Yarn_5_test

        # Get the result from the tested sample
        file = open_file(filename)
        # grid = identify_board(file)
        block_type, block_amount = identify_blocks(file)
        lazor_start = identify_lazor_start(file)
        lazor_points = identify_lazor_points(file)

    def TestA(self):
        # Test 'Block' class by testing whether refractive block reflects laser
        self.assertEqual(example_test[0], block_type,
                         msg='Error: block reading incorrect')

    def TestB(self):
        self.assertEqual(example_test[1], block_amount，, msg='Error: block reading incorrect')

    def TestC(self):
        self.assertEqual(
            example_test[2], lazor_start, msg='Error: Block does not return correct laser')

    def TestD(self):
        self.assertEqual(example_test[3], lazor_points)

    # Test 'get_colors' function
    def TestE(self):
        color_test = get_colors()
        assert (color_test['B'] == (0, 0, 0)
                ), 'Error: get_colors() return incorrect'
    
    # Test 'save_grid' function
    def TestF(self):
        save_grid(mad_1_test[0], 'test')
        img_test = Image.open('test_solution.png')
        assert(img_test.getpixel((15, 15)) == (50, 50, 50)
               ), 'Error: save_image does not save correct image'


if __name__ == "__main__":
    unittest.main()
