import copy

import chip
class GameState(object):
    def __init__(self,*args):
        if len(args) == 0:
            self._chips = [[0 for x in range(8)] for y in range(8)]
            for i in range(8):
                for j in range(8):
                    self._chips[i][j] = chip.Chip(i,j,"-")

            self._chips[3][3].color = "w"
            self._chips[4][4].color = "w"
            self._chips[4][3].color = "b"
            self._chips[3][4].color = "b"

        else:
            self._chips = copy.deepcopy(args[0])
            self._chips[int(args[1])][int(args[2])].color = args[3]


    @property
    def chips(self):
        return self._chips

    def __int__(self,current,new_x,new_y,color):
        self._chips = current.chips
        self._chips[new_x][new_y].color = color




    def print_state(self):
        for i in range(8):
            for j in range(8):
                print(str(self._chips[i][j]), end=" ")
            print()
        print()
#TODO napravi equals




