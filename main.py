from window import Window
from maze import Maze
import sys

def main():

    num_rows = 16
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = int((screen_x - 2 * margin) / num_cols)
    cell_size_y = int((screen_y - 2 * margin) / num_rows)

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze cannot be solved")
    else:
        print("maze solved!")
    win.wait_for_close()

main()