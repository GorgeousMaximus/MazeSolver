from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(
            master=self.__root, bg="white", width=width, height=height
        )
        self.__canvas.pack(side="left", expand=True, fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: "Line", fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y


class Line:
    def __init__(self, start: Point, finish: Point) -> None:
        self._start = start
        self._finish = finish

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
            self._start.x,
            self._start.y,
            self._finish.x,
            self._finish.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    def __init__(self, window: Window | None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0
        self.__win = window
        self.__visited = False

    def draw(self, x1: float, x2: float, y1: float, y2: float) -> None:
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_top_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "white"
            )
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "white"
            )
        if self.has_left_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "white"
            )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            )
        else:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "white"
            )

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        if self.__win is None:
            return
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        this_midpoint = self.get_midpoint()
        to_midpoint = to_cell.get_midpoint()
        line = Line(
            Point(this_midpoint[0], this_midpoint[1]),
            Point(to_midpoint[0], to_midpoint[1]),
        )
        self.__win.draw_line(line, fill_color)

    def get_midpoint(self) -> tuple[float, float]:
        mid_x = (self.__x1 + self.__x2) / 2
        mid_y = (self.__y1 + self.__y2) / 2
        return (mid_x, mid_y)

    def is_visited(self) -> bool:
        return self.__visited

    def visit(self) -> None:
        self.__visited = True

    def reset_visited(self) -> None:
        self.__visited = False
