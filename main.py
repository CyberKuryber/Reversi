import gameState
import tree
import treeNode
import alphabeta
import heuristic
from time import time
import hashingMap


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = gameState.GameState()
    main_tree = tree.Tree()
    main_tree.root = treeNode.TreeNode(None, p)
    current = main_tree.root
    self = 'b'
    opp = 'w'
    counter = 4
    changed_turn = False
    game_map = hashingMap.ChainedHashMap(3*64)
    #heuristic.build_children(self,opp,current,game_map)
    search = alphabeta.AlphaBeta(main_tree)

   # heuristic.build_children('w','b',current)
    while True:

        if counter<=10 or counter>=50:
            depth = 3
        else:
            depth = 2

        start = time()
        main_tree.build_tree(current, self, opp, depth, game_map)

        if current.is_leaf():
            if changed_turn:
                # kraj igre
                break
            else:
                changed_turn = True
        else:
            changed_turn = False

            if self == 'b':
                while True:
                    print("Unesite broj vaseg poteza")
                    current.view_possible()
                    choice=input("\n")
                    try:
                        choice = int(choice)
                        choice -= 1
                        if choice < len(current.children):
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Pogresan unos pokusajte ponovo")

                #choice=0
                current = current.children[choice]
                current.grid.print_state()
            else:

                x = search.alpha_beta_search(current)
                current = x
                print("Racunar je odigrao")
                current.grid.print_state()

        #main_tree.breadth_first()
            stop = time()
            print("Potrebno vreme: ",stop-start)

        self, opp = opp, self
        counter += 1

    num_white=0
    num_black=0
    for i in range(8):
        for j in range(8):
            if current.grid.chips[i][j].color == 'w':
                num_white +=1
            if current.grid.chips[i][j].color == 'b':
                num_black += 1


    if num_white>num_black:
        print("Beli je pobednik")
    else:
        print("Crni je pobednik")









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
