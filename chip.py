class Chip(object):

    def __init__(self, x, y, color="-"):
        self._x = x
        self._y = y
        self._color =  color


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color

    def color_swap(self):
        if self._color == "b":
            self._color = "w"
            return None

        if self._color == "w":
            self._color = "b"
            return None

    def __str__(self):
        if self._color == "b":
            return "B"
        if self._color == "w":
            return "W"
        return "-"
"""
    def __eq__(self, other):
        self._color == other._color
"""