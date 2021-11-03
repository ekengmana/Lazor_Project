# This file takes in a .bff file and reads it out
# Functions will be to read it in, split it by line


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
        x = str(line.split("\n"))
        x = x.strip("['").strip("']").strip("',")
        # print(x)
        if x[0][0] == '#' or x[0][0] == ' ':
            continue
        else:
            split_fptr.append(x)

    return split_fptr

def identify_blocks(fptr_lines, start_line):
    block_type = []
    block_amount = []
    line_count = start_line
    # print(start_line)
    for i in range(start_line, len(fptr_lines)):
        # print(i)
        if 'L' in fptr_lines[i]:
            line_count = i
            break
        elif 'A' or 'B' or 'C' in fptr_lines[i]:
            line = str(fptr_lines[i])
            block_type.append(line[0])
            block_amount.append(line[2])
    return block_type, block_amount, line_count
    


def identify_lazor_start(fptr_lines, start_line):
    lazor_point = []
    angle = []
    line_count = start_line
    for i in range(start_line, len(fptr_lines)):
        # print(fptr_lines[i])
        if 'P' in fptr_lines[i]:
            line_count = i
            break
        elif 'L' in fptr_lines[i]:
            # print(fptr_lines[i])
            line = str(fptr_lines[i])
            lazor_point.append((int(line[2]), int(line[4])))
            if line[6] == '-' and line[9] == '-':
                angle.append((-1 * int(line[7]), -1 * int(line[10])))
            elif line[6] == '-':
                angle.append((-1 * int(line[7]), int(line[9])))
            elif line[8] == '-':
                angle.append((int(line[6]), -1 * int(line[9])))
            else:
                angle.append((int(line[6]), int(line[8])))
    return lazor_point, angle, line_count


def identify_lazor_points(fptr_lines, start_line):
    lazor_point = []
    for i in range(start_line, len(fptr_lines)):
        if 'P' in fptr_lines[i]:
            line = str(fptr_lines[i])
            lazor_point.append((int(line[2]), int(line[4])))
    return lazor_point

def identify_board(fptr_lines):
    '''
    Identifies the grid size and returns a grid with the corresponding size
    **Parameters**
        fptr_lines: *list, str*
            a list of different strings from the .bff file
    **Returns**
        grid: *list, str*
            the size of the grid in the .bff file
        line_count: *int*
            a line counter to keep track of what lines to skip over in remaining file reads
    '''
    line_count = 0
    grid = []
    # print(column)
    for i in range(len(fptr_lines)):
        # parse through the list
        # print(fptr_lines[i])
        if 'GRID STOP' in fptr_lines[i]:
            # no need to continue since grid is already identified
            line_count = i
            break
        elif 'GRID START' in fptr_lines[i]:
            # identifies the start of the grid
            # fptr_lines.remove(fptr_lines[i])
            continue
        line = str(fptr_lines[i])
        # print(line)
        grid.append(line)
    return grid, (line_count + 1)
            

if __name__ == '__main__':
    fptr = open('mad_7.bff', 'r')
    fptr_lines = split_by_line(fptr)
    # print(fptr_lines)
    grid, line_count1 = identify_board(fptr_lines)
    # print(line_count1)
    block_type, block_amount, line_count2= identify_blocks(fptr_lines, line_count1)
    lazor_start, angle, line_count3 = identify_lazor_start(fptr_lines, line_count2)
    lazor_points = identify_lazor_points(fptr_lines, line_count3)
    print(grid)
    print(block_type)
    print(block_amount)
    print(lazor_start)
    print(angle)
    print(lazor_points)
    