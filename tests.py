import unittest

from src.maze import Maze
from src.cells import Cell


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )

    def test_cell_initial_walls_are_true(self):
        c1 = Cell()
        self.assertTrue(c1.has_left_wall)
        self.assertTrue(c1.has_right_wall)
        self.assertTrue(c1.has_top_wall)
        self.assertTrue(c1.has_bottom_wall)

    def test_maze_dimensions_match_cell_grid(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(m1.num_cols, num_cols)
        self.assertEqual(m1.num_rows, num_rows)
        self.assertEqual(m1.cell_size_x, cell_size_x)
        self.assertEqual(m1.cell_size_y, cell_size_y)

    def test_entrance_and_exit_walls(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Check if the entrance and exit walls are broken
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[num_rows - 1][num_cols - 1].has_bottom_wall)

    def test_reset_visited_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Mark some cells as visited
        m1._Maze__cells[0][0].visited = True
        m1._Maze__cells[1][1].visited = True
        # Reset visited cells
        m1.reset_visited()
        # Check if all cells are reset to not visited
        for row in m1._Maze__cells:
            for cell in row:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
