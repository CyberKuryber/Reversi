import gameState
import treeNode


def canmove(self, opp, pomocni_string):
    if pomocni_string[0] != opp:
        return False

    for ctr in range(7):
        if pomocni_string[ctr] == '-':
            return False
        if (pomocni_string[ctr] == self):
            return True

    return False


def isLegalMove(self, opp, grid, startx, starty):
    if grid[startx][starty].color != '-':
        return False
    pomocni_string = ""
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            # keep going if both velocities are zero
            if not (dy) and not (dx):
                continue
            #		pomocni_string[0] = '\0'
            for ctr in range(1, 8):
                x = startx + ctr * dx
                y = starty + ctr * dy
                if (x >= 0 and y >= 0 and x < 8 and y < 8):
                    pomocni_string = pomocni_string[:ctr - 1] + grid[x][y].color + pomocni_string[ctr:]
                else:
                    pomocni_string = pomocni_string[:ctr - 1] + "0" + pomocni_string[ctr:]

            if (canmove(self, opp, pomocni_string)): return True

    return False


def num_valid_moves(self, opp, grid):
    count = 0
    for i in range(8):
        for j in range(8):
            if (isLegalMove(self, opp, grid, i, j)): count += 1
    return count


def build_children(self, opp, current_node,game_map):
    for i in range(8):
        for j in range(8):
            if (isLegalMove(self, opp, current_node.grid.chips, i, j)):
                child = treeNode.TreeNode(current_node, gameState.GameState(current_node.grid.chips, i, j, self))
                correct(child.grid, self, opp, i, j)
                child.value=game_map[game_map.generate_hash_value(child.grid.chips)]
                if child.value is None:
                    child.value = dynamic_heuristic_evaluation_function(child.grid.chips, self, opp)
                    game_map[game_map.generate_hash_value(child.grid.chips)] = child.value
                if self == 'b': child.value *= -1
                current_node.children.append(child)


def correct(state, self, opp, startx, starty):

    for k in range(8):
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j ==0: continue
                swapable = []
                x = startx
                y = starty
                while (x + i) >=0 and (x + i) <8 and (y + j) >=0 and (y + j) <8:
                    if state.chips[x + i][y + j].color == opp:
                        swapable.append(state.chips[x + i][y + j])
                        x+=i
                        y+=j

                    elif state.chips[x + i][y + j].color == self:
                        if len(swapable) !=0:
                            for k in swapable:
                                k.color_swap()
                        break
                    elif state.chips[x + i][y + j].color == "-":
                        break



"""
 * Assuming my_color stores your color and opp_color stores opponent's color
 * '-' indicates an empty square on the board
 * 'b' indicates a black tile and 'w' indicates a white tile on the board
 */

 """


def dynamic_heuristic_evaluation_function(grid, my_color, opp_color):
    my_tiles = opp_tiles = my_front_tiles = opp_front_tiles = 0
    p = c = l = m = f = d = 0
    #my_color='w'
    #opp_color='b'

    X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    Y1 = [0, 1, 1, 1, 0, -1, -1, -1]
    V = [[20, -3, 11, 8, 8, 11, -3, 20], [-3, -7, -4, 1, 1, -4, -7, -3], [1, -4, 2, 2, 2, 2, -4, 11],
         [8, 1, 2, -3, -3, 2, 1, 8], [8, 1, 2, -3, -3, 2, 1, 8], [11, -4, 2, 2, 2, 2, -4, 11],
         [-3, -7, -4, 1, 1, -4, -7, -3], [20, -3, 11, 8, 8, 11, -3, 20]]

    # // Piece difference, frontier disks and disk squares
    for i in range(8):
        for j in range(8):
            if grid[i][j].color == my_color:
                d += V[i][j]
                my_tiles += 1
            elif (grid[i][j].color == opp_color):
                d -= V[i][j]
                opp_tiles += 1

            if grid[i][j] != '-':
                for k in range(8):
                    x = i + X1[k]
                    y = j + Y1[k]
                    if (x >= 0 and x < 8 and y >= 0 and y < 8 and grid[x][y].color == '-'):
                        if (grid[i][j].color == my_color):
                            my_front_tiles += 1
                        else:
                            opp_front_tiles += 1
                        break

    if (my_tiles > opp_tiles):
        p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
    elif (my_tiles < opp_tiles):
        p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        p = 0

    if (my_front_tiles > opp_front_tiles):
        f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
    elif (my_front_tiles < opp_front_tiles):
        f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
    else:
        f = 0

    # // Corner occupancy
    my_tiles = opp_tiles = 0
    if (grid[0][0].color == my_color):
        my_tiles += 1
    elif (grid[0][0].color == opp_color):
        opp_tiles += 1
    if (grid[0][7].color == my_color):
        my_tiles += 1
    elif (grid[0][7].color == opp_color):
        opp_tiles += 1
    if (grid[7][0].color == my_color):
        my_tiles += 1
    elif (grid[7][0].color == opp_color):
        opp_tiles += 1
    if (grid[7][7].color == my_color):
        my_tiles += 1
    elif (grid[7][7].color == opp_color):
        opp_tiles += 1
    c = 25 * (my_tiles - opp_tiles)

    # // Corner closeness
    my_tiles = opp_tiles = 0
    if (grid[0][0].color == '-'):
        if (grid[0][1].color == my_color):
            my_tiles += 1
        elif (grid[0][1].color == opp_color):
            opp_tiles += 1
        if (grid[1][1].color == my_color):
            my_tiles += 1
        elif (grid[1][1].color == opp_color):
            opp_tiles += 1
        if (grid[1][0].color == my_color):
            my_tiles += 1
        elif (grid[1][0].color == opp_color):
            opp_tiles += 1

    if (grid[0][7].color == '-'):
        if (grid[0][6].color == my_color):
            my_tiles += 1
        elif (grid[0][6].color == opp_color):
            opp_tiles += 1
        if (grid[1][6].color == my_color):
            my_tiles += 1
        elif (grid[1][6].color == opp_color):
            opp_tiles += 1
        if (grid[1][7].color == my_color):
            my_tiles += 1
        elif (grid[1][7].color == opp_color):
            opp_tiles += 1

    if (grid[7][0].color == '-'):
        if (grid[7][1].color == my_color):
            my_tiles += 1
        elif (grid[7][1].color == opp_color):
            opp_tiles += 1
        if (grid[6][1].color == my_color):
            my_tiles += 1
        elif (grid[6][1].color == opp_color):
            opp_tiles += 1
        if (grid[6][0].color == my_color):
            my_tiles += 1
        elif (grid[6][0].color == opp_color):
            opp_tiles += 1

    if (grid[7][7].color == '-'):
        if (grid[6][7].color == my_color):
            my_tiles += 1
        elif (grid[6][7].color == opp_color):
            opp_tiles += 1
        if (grid[6][6].color == my_color):
            my_tiles += 1
        elif (grid[6][6].color == opp_color):
            opp_tiles += 1
        if (grid[7][6].color == my_color):
            my_tiles += 1
        elif (grid[7][6].color == opp_color):
            opp_tiles += 1

    l = -12.5 * (my_tiles - opp_tiles)



    # // Mobility
    my_tiles = num_valid_moves(my_color, opp_color, grid)
    opp_tiles = num_valid_moves(opp_color, my_color, grid)
    if (my_tiles > opp_tiles):
        m = (100.0 * my_tiles) / (my_tiles + opp_tiles)
    elif (my_tiles < opp_tiles):
        m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
    else:
        m = 0

    # // final weighted score
    score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d)
    return score
