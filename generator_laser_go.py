import copy


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
    target_pool = copy.copy(target_position)
    for curr_pos in lazor_origin:
        lazor_pos_list.append([curr_pos])

    all_meet = False

    while not all_meet:
        n = n + 1
        for i in range(len(lazor_pos_list)):
            if len(lazor_pos_list[i][-1] == 0):
                continue
            curr_pos, curr_dirc = lazor_pos_list[j][-1][0], lazor_pos_list[j][-1][1]

            if not position_chk(board, position):
                if n > 1:
                    lazor_pos_list[i].append([])
                    continue

            next_dir = lazor_check(board, curr_pos, curr_dirc)

            if len(next_dir) == 1:
                curr_dirc = next_dirc[0]
                curr_pos = tuple(map(sum, zip(curr_pos, curr_dirc)))
                lazor_pos_list[i].append([curr_pos, curr_dirc])

            elif len(next_dir) == 2:
                dir_one, dir_two = next_dirt[0], next_dir[1]
                pos_one = tuple(map(sum, zip(curr_pos, dir_one)))
                pos_two = tuple(map(sum, zip(curr_pos, dir_two)))
                lazor_pos_list[i].append([pos_one, dir_one])
                lazor_pos_list.append([[pos_two, dir_two]])
            else:
                lazor_pos_list[i].append([])

            # See if all the target position come to lisr
            lazor_in_list = 0
            for lazor_i in lazor_pos_list:
                if len(lazor_i[-1]) != 0:
                    lazor_in_list = lazor_in_list + 1

            if lazor_in_list == 0:
                break
            if n == max_n:
                break

        for lazor_i in lazor_pos_list:
            for positions in lazor_i:
                try:
                    if position[0] in target_pool:
                        target_pool.remove(positions[0])
                except IndexError:
                    pass

    if len(target_pool) == 0:
        return True
    else:
        return False
