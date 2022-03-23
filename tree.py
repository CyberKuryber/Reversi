"""
Modul sadrži implementaciju stabla.
"""
from moj_queue import Moj_queue
import heuristic
from treeNode import TreeNode


class Tree(object):
    """
    Klasa modeluje stablo.
    """
    def __init__(self):
        self._root = None

    def is_empty(self):
        """
        Metoda proverava da li stablo ima elemenata.
        """
        return self._root is None

    def depth(self, x):
        """
        Metoda izračunava dubinu zadatog čvora.

        Argument:
        - `x`: čvor čija dubina se računa
        """
        if x.is_root():
            return 0
        else:
            return 1 + self.depth(x.parent)

    def _height(self, x):
        """
        Metoda izračunava visinu podstabla sa zadatim korenom.

        Argument:
        - `x`: koren posmatranog podstabla
        """
        if x.is_leaf():
            return 0
        else:
            return 1 + max(self._height(c) for c in x.children)

    def height(self):
        return self._height(self._root)

    def preorder(self, x):
        """
        Preorder obilazak po dubini

        Najpre se vrši obilazak roditelja a zatim svih njegovih potomaka.

        Argument:
        - `x`: čvor od koga počinje obilazak
        """
        if not self.is_empty():

            x.grid.print_state()
            for c in x.children:
                self.preorder(c)

    def postorder(self, x):
        """
        Postorder obilazak po dubini

        Najpre se vrši obilazak potomaka a zatim i roditelja

        Argument:
        - `x`: čvor od koga počinje obilazak
        """
        if not self.is_empty():
            for c in x.children:
                self.postorder(c)
            print(x.data)

    def breadth_first(self):
        """
        Metoda vrši obilazak stabla po širini.
        """
        to_visit = Moj_queue()
        to_visit.enqueue(self._root)
        while not to_visit.is_empty():
            e = to_visit.dequeue()
            e.grid.print_state()
            print(e.value)

            for c in e.children:
                to_visit.enqueue(c)

    def build_tree(self,current,me,opp, max_depth,game_map):
        #max_depth -=1
        if max_depth == 0:
            return None
        else:
            if len(current.children) == 0:
                heuristic.build_children(me, opp, current,game_map)
            for c in current.children:
                self.build_tree(c,opp, me,max_depth-1,game_map)


    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

