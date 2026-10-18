from graphics import Window, Point, Line, Cell
from maze import Maze


def main():
    seed = int(input("Select a seed (please stick to integers for now): "))
    WIDTH, HEIGHT = 800, 600
    grid_size = min(WIDTH, HEIGHT)
    grid_margin = 50
    num_rows = 10
    num_cols = 5
    cell_size = (grid_size - (2 * grid_margin)) / max(num_cols, num_rows)
    margin_x = (WIDTH - (cell_size * num_cols)) // 2
    margin_y = (HEIGHT - (cell_size * num_rows)) // 2
    win = Window(WIDTH, HEIGHT)
    maze = Maze(margin_x, margin_y, num_rows, num_cols, cell_size, cell_size, win, seed)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
