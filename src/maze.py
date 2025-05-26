# python import
import time
from typing import Optional, List
import random

# application imports
from src.gui_graphics import Window, Line, Point, CATPPUCCIN
from src.cells import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Optional[Window] = None,
        seed: Optional[int] = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__cells = []
        self.__win = win
        if seed is not None:
            random.seed(seed)
        self.seed = seed
        self.__create_cells()
        self.__break_walls_r(0, 0)  # Start breaking walls from the top-left cell
        self.reset_visited()

    def __create_cells(self):
        """
        Create a grid of cells based on the specified number of rows and columns.
        Each cell is an instance of the Cell class, which is drawn on the window.
        The cells are stored in a 2D list (list of lists).
        """
        self.__cells = [[Cell(self.__win) for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cell(i, j)

        # draw entrance and exit
        self.__break_entrance_and_exit()

    def __draw_cell(self, i, j):
        """
        Draw a cell at the given row and column indicx
            Calculate the x/y position of the element in the grid.
        :param i: Row index of the cell.
        :param j: Column index of the cell.
        """
        if 0 <= i < self.num_rows and 0 <= j < self.num_cols:
            if self.__win is None:
                return
            cell = self.__cells[i][j]
            x1 = self.x1 + j * self.cell_size_x
            y1 = self.y1 + i * self.cell_size_y
            cell.draw(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y)
            self.__animate()

    def __animate(self):
        """
        Call the window's redraw method
        Sleep for a short time to allow the GUI to update.
        """
        if self.__win is not None:
            self.__win.redraw()
            time.sleep(0.01)  # Adjust the sleep time as needed for animation speed

    def __break_entrance_and_exit(self):
        """
        Break the entrance and exit walls of the maze.
        """
        # Example: Break the top-left cell's top wall and bottom-right cell's bottom wall
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        if self.__win is not None:
            # Redraw the entrance and exit cells to reflect the changes
            self.__draw_cell(0, 0)
            self.__draw_cell(self.num_rows - 1, self.num_cols - 1)

    def __break_walls_r(self, i, j):
        """
        Depth-first traversal through the maze to break walls and create paths.
        :param i: Current row index.
        :param j: Current column index.
        """
        self.__cells[i][j].visited = True

        while True:
            possible_directions = []
            # Check if the neighboring cell exists andhas not been visited
            # Check all four possible directions (up, down, left, right)
            # If so, append (neighbor_i, neighbor_j) to possible_directions
            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i < self.num_rows - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j < self.num_cols - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            if not possible_directions:
                # draw current cell and return
                self.__draw_cell(i, j)
                return
            else:
                # Choose a random direction from the possible_directions list
                # knock down the wall between the current cell and the chosen neighbor
                neighbor_i, neighbor_j = random.choice(possible_directions)
                if neighbor_i < i:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[neighbor_i][neighbor_j].has_bottom_wall = False
                elif neighbor_i > i:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[neighbor_i][neighbor_j].has_top_wall = False
                elif neighbor_j < j:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[neighbor_i][neighbor_j].has_right_wall = False
                elif neighbor_j > j:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[neighbor_i][neighbor_j].has_left_wall = False
                # Draw the current cell and the neighbor cell
                self.__draw_cell(i, j)
                # Recursively call __break_walls_r on the neighbor cell
                self.__break_walls_r(neighbor_i, neighbor_j)

    def reset_visited(self):
        """
        Reset the visited status of all cells in the maze.
        This is useful for algorithms that need to traverse the maze multiple times.
        """
        for row in self.__cells:
            for cell in row:
                cell.visited = False

    def solve(self) -> bool:
        """
        Public method to solve the maze from entrance (0, 0) to exit (bottom-right).
        """
        return self.__solve_r(0, 0)

    def __solve_r(self, i: int, j: int) -> bool:
        """
        Recursive depth-first search maze solver.
        """
        current = self.__cells[i][j]
        self.__animate()
        current.visited = True

        # Base case: if we're at the exit
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        # Direction vectors: (delta_i, delta_j, direction)
        directions = [
            (-1, 0, "top"),
            (1, 0, "bottom"),
            (0, -1, "left"),
            (0, 1, "right"),
        ]

        for di, dj, direction in directions:
            ni, nj = i + di, j + dj
            if not self.__is_valid_move(i, j, ni, nj, direction):
                continue

            next_cell = self.__cells[ni][nj]
            current.draw_move(next_cell)
            if self.__solve_r(ni, nj):
                return True
            current.draw_move(next_cell, undo=True)

        return False

    def __is_valid_move(self, i, j, ni, nj, direction) -> bool:
        """
        Checks if moving from (i, j) to (ni, nj) in given direction is valid.
        """
        if ni < 0 or ni >= self.num_rows or nj < 0 or nj >= self.num_cols:
            return False

        neighbor = self.__cells[ni][nj]
        if neighbor.visited:
            return False

        current = self.__cells[i][j]

        if direction == "top" and not current.has_top_wall:
            return True
        if direction == "bottom" and not current.has_bottom_wall:
            return True
        if direction == "left" and not current.has_left_wall:
            return True
        if direction == "right" and not current.has_right_wall:
            return True

        return False

    @property
    def cells(self) -> List[List[Cell]]:
        """
        Get the 2D list of cells in the maze.
        :return: A 2D list of Cell objects representing the maze.
        """
        return self.__cells

    @property
    def width(self) -> int:
        """
        Get the width of the maze in pixels.
        :return: The width of the maze in pixels.
        """
        return self.num_cols * self.cell_size_x

    @property
    def height(self) -> int:
        """
        Get the height of the maze in pixels.
        :return: The height of the maze in pixels.
        """
        return self.num_rows * self.cell_size_y
