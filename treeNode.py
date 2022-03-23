class TreeNode(object):
    """
    Klasa modeluje čvor stabla.
    """

    def __init__(self,parent,grid):
        """
        Konstruktor.

        Argument:
        - `data`: podatak koji se upisuje u čvor
        """
        self._grid = grid
        self._parent = parent
        self._children = []
        self._value = None #ne bi smelo da se desava

    def is_root(self):
        """
        Metoda proverava da li je čvor koren stabla.
        """
        return self._parent is None

    def is_leaf(self):
        """
        Metoda proverava da li je čvor list stabla.
        """
        return len(self.children) == 0

    def add_child(self, x):

        x.parent = self
        self.children.append(x)

    def __str__(self):
        return str(self.grid)

    def view_possible(self):
        possible = [[0 for x in range(8)] for y in range(8)]

        for i in range(8):
            for j in range(8):
                possible[i][j] = str(self.grid.chips[i][j])

        for k in range(len(self.children)):
            for i in range(8):
                for j in range(8):
                    if str(self.children[k].grid.chips[i][j])!='-' and possible[i][j] == '-':
                        possible[i][j] = str(k+1)

        for i in range(8):
            for j in range(8):
                print(str(possible[i][j]), end=" ")
            print()
        print()




    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def children(self):
        return self._children

    @property
    def grid(self):
        return self._grid
