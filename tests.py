import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_B(self):
        num_cols = 20
        num_rows = 30
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_C(self):
        num_cols = 2
        num_rows = 1
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._Maze__cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_rows = 5
        num_cols = 5
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m4._Maze__break_entrance_and_exit()
        self.assertEqual(
            m4._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m4._Maze__cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        num_rows = 4
        num_cols = 3
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m5._Maze__cells:
            for cell in col:
                cell.visit()
        m5._Maze__reset_cells_visited()
        for col in m5._Maze__cells:
            for cell in col:
                self.assertEqual(
                    cell.is_visited(),
                    False,
                )


if __name__ == "__main__":
    unittest.main()
