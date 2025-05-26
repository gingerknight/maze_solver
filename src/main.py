# Maze Solver
from src.gui_graphics import Window
from src.cells import Cell
from src.maze import Maze


def main():
    # Create a window with specified dimensions
    window = Window(800, 600)

    # create a 2x2 grid of cells
    cell_size_x = 25
    cell_size_y = 25
    num_rows = 10
    num_cols = 15
    x1 = 50
    y1 = 50
    cells = []
    # def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window):
    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window)

    # Solve the maze
    maze.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()
# This is the main entry point for the Maze Solver application.
# It initializes the window and starts the event loop.
# The window will remain open until the user closes it.
