import random
import time
from graphics import Cell, Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window | None = None,
        seed=None,
    ) -> None:
        self.__x1: int = x1
        self.__y1: int = y1
        self.__num_rows: int = num_rows
        self.__num_cols: int = num_cols
        self.__cell_size_x: float = cell_size_x
        self.__cell_size_y: float = cell_size_y
        self.__win: Window | None = win
        self.__cells: list[list[Cell]] = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed is not None:
            self.__seed = random.seed(seed)
        self.__break_walls_r(0, 0)

    def __create_cells(self) -> None:
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j) -> None:
        cell_x1 = self.__x1 + (i * self.__cell_size_x)
        cell_y1 = self.__y1 + (j * self.__cell_size_y)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y2 = cell_y1 + self.__cell_size_y
        self.__cells[i][j].draw(cell_x1, cell_x2, cell_y1, cell_y2)
        self.__animate()

    def __animate(self) -> None:
        if self.__win:
            self.__win.redraw()
            time.sleep(0.03)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visit()
        neighbours = []
        if i > 0 and not self.__cells[i - 1][j].is_visited():
            neighbours.append((i - 1, j))
        if i < len(self.__cells) - 1 and not self.__cells[i + 1][j].is_visited():
            neighbours.append((i + 1, j))
        if j > 0 and not self.__cells[i][j - 1].is_visited():
            neighbours.append((i, j - 1))
        if j < len(self.__cells[i]) - 1 and not self.__cells[i][j + 1].is_visited():
            neighbours.append((i, j + 1))
        while True:
            if not neighbours:
                self.__draw_cell(i, j)
                return
            direction = random.choice(neighbours)
            neighbours.remove(direction)
            if self.__cells[direction[0]][direction[1]].is_visited():
                continue
            if direction[0] < i:
                self.__cells[i][j].has_left_wall = False
                self.__cells[direction[0]][direction[1]].has_right_wall = False
            if direction[0] > i:
                self.__cells[i][j].has_right_wall = False
                self.__cells[direction[0]][direction[1]].has_left_wall = False
            if direction[1] < j:
                self.__cells[i][j].has_top_wall = False
                self.__cells[direction[0]][direction[1]].has_bottom_wall = False
            if direction[1] > j:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[direction[0]][direction[1]].has_top_wall = False
            self.__break_walls_r(direction[0], direction[1])

    def __reset_cells_visited(self) -> None:
        for col in self.__cells:
            for cell in col:
                cell.reset_visited()

    def solve(self) -> bool:
        random.seed()
        self.__reset_cells_visited()
        return self.__solve_r(0, 0)

    def __solve_r(self, i: int, j: int) -> bool:
        self.__animate()
        self.__cells[i][j].visit()
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        neighbours = []
        if (
            i > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].is_visited()
        ):
            neighbours.append((i - 1, j))
        if (
            i < len(self.__cells) - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].is_visited()
        ):
            neighbours.append((i + 1, j))
        if (
            j > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].is_visited()
        ):
            neighbours.append((i, j - 1))
        if (
            j < len(self.__cells[i]) - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].is_visited()
        ):
            neighbours.append((i, j + 1))

        while True:
            if not neighbours:
                return False
            direction = random.choice(neighbours)
            neighbours.remove(direction)
            self.__cells[i][j].draw_move(self.__cells[direction[0]][direction[1]])
            result = self.__solve_r(direction[0], direction[1])
            if result:
                return result
            else:
                self.__cells[i][j].draw_move(
                    self.__cells[direction[0]][direction[1]], True
                )
