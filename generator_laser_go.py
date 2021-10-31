import copy


def laser_go(board, laser_origin, target_position):
    '''
    Organize the board, and get the lasers running from
    a start position tothe end position.
    During this period, every laser's position will be checked
    to make sure it goes through the certain target spot.

    **Parameters**
        board: *list, list, string*
            Where those spot located, which will show as the form of a list
            indicating the type of those blocks

        laser_origin: *list, list, tuple, int*
            Those lists shows the laser's starting position.
            And the other list is the laser's original position

        target_position: *list, tuple, int*
            The intersections position where the laser meet with those wall

    **Returns**
        *boolean*
            The judgment statement of whether the laser are intersected with
            all the target position. If all target position get meet, then
            they get the True as a feedback.

    '''

    n = 0
    max_n = 1000

    laser_pos_list = []
    target_pool = copy.copy(target_position)
    for curr_pos in laser_origin:
        laser_pos_list.append([curr_pos])

    all_meet = False

    while not all_meet:
        n = n + 1
        for i in range(len(laser_pos_list)):
            if len(laser_pos_list[i][-1] == 0):
                continue
            curr_pos, curr_dirc = laser_pos_list[j][-1][0], laser_pos_list[j][-1][1]

            if not position_chk(board, position):
                if n > 1:
                    laser_pos_list[i].append([])
                    continue

            next_dir = laser_check(board, curr_pos, curr_dirc)

            if len(next_dir) == 1:
                curr_dirc = next_dirc[0]
                curr_pos = tuple(map(sum, zip(curr_pos, curr_dirc)))
                laser_pos_list[i].append([curr_pos, curr_dirc])

            elif len(next_dir) == 2:
                dir_one, dir_two = next_dirt[0], next_dir[1]
                pos_one = tuple(map(sum, zip(curr_pos, dir_one)))
                pos_two = tuple(map(sum, zip(curr_pos, dir_two)))
                laser_pos_list[i].append([pos_one, dir_one])
                laser_pos_list.append([[pos_two, dir_two]])
            else:
                laser_pos_list[i].append([])

            # See if all the target position come to lisr
            laser_in_list = 0
            for laser_i in laser_pos_list:
                if len(laser_i[-1]) != 0:
                    laser_in_list = laser_in_list + 1

            if laser_in_list == 0:
                break
            if n == max_n:
                break

        for laser_i in laser_pos_list:
            for positions in laser_i:
                try:
                    if position[0] in target_pool:
                        target_pool.remove(positions[0])
                except IndexError:
                    pass

    if len(target_pool) == 0:
        return True
    else:
        return False
