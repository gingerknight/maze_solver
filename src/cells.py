# python imports
from typing import Optional

# application imports
from src.gui_graphics import Window, Line, Point, CATPPUCCIN


class Cell:
    def __init__(self, window: Optional[Window] = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        Updates internal x/y coordinates and draws itself on the canvas (window).
        """
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), CATPPUCCIN["wall"])
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), CATPPUCCIN["wall"])
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), CATPPUCCIN["wall"])
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), CATPPUCCIN["wall"])

        # If a wall doesn't exist, draw a "background" colored line
        if not self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), CATPPUCCIN["background"])
        if not self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), CATPPUCCIN["background"])
        if not self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), CATPPUCCIN["background"])
        if not self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), CATPPUCCIN["background"])

    def draw_move(self, to_cell, undo=False) -> None:
        """
        Draws a move from this cell to another cell.

        :param to_cell: The cell to which the move is being made.
        :param undo: If True draw line in CATPPUCCIN["path"], otherwise CATPPUCCIN["highlight"]
        """
        if self.__win is None:
            return
        # from point of view of this cell, draw a line to the other cell
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1
        # find center of destination cell
        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        if undo:
            self.__win.draw_line(Line(Point(x_center, y_center), Point(x_center2, y_center2)), CATPPUCCIN["path"])
        else:
            self.__win.draw_line(Line(Point(x_center, y_center), Point(x_center2, y_center2)), CATPPUCCIN["highlight"])
