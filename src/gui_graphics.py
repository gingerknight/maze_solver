# Maze Solver
from tkinter import Tk, Canvas

# Catpuccin theme for colors
CATPPUCCIN = {
    "background": "#313244",
    "wall": "#89b4fa",
    "path": "#cba6f7",
    "visited": "#eba0ac",
    "start": "#94e2d5",
    "end": "#a6e3a1",
    "highlight": "#f9e2af",
}


class Point:
    """A simple class to represent a point in 2D space.
    The value x=0 is the left of the screen, y=0 is the top of the screen.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        """
        Draw the line on the provided canvas.
        :param canvas: The canvas to draw on.
        :param fill_color: The color to fill the line with. Defaults to "black".
        """
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg=CATPPUCCIN["background"])
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        """
        Redraw all the graphics in the window.
        The assumption is their positions and colors may have changed.
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        """
        Wait for the window to be closed.
        """
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed.")

    def close(self) -> None:
        """
        Close the window.
        """
        self.__running = False

    def draw_line(self, line: Line, fill_color) -> None:
        """
        Draw a line on the canvas.
        :param Line: The line to draw, which should have a start and end Point.
        :param fill_color: The color to fill the line with.
        """
        line.draw(self.__canvas, fill_color)
