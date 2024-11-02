from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
            ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win)  # Instantiate the Cell object
                col_cells.append(cell)  # Add the Cell to the column
            self._cells.append(col_cells)  # Add the column to the matrix
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if j + 1 < self._num_rows:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            if i + 1 < self._num_cols:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            if not to_visit:
                self._draw_cell(i, j)
                return
            direction = random.randint(0, len(to_visit) - 1)
            new_i = to_visit[direction][0]
            new_j = to_visit[direction][1]

            if new_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if new_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if new_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if new_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # left
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i - 1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            test_left = self._solve_r(i - 1, j)
            if test_left:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # right
        if i < self._num_cols - 1 and self._cells[i][j].has_right_wall == False and self._cells[i + 1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            test_right = self._solve_r(i + 1, j)
            if test_right:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # up
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j - 1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            test_up = self._solve_r(i, j - 1)
            if test_up:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # down
        if j < self._num_rows - 1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j + 1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            test_down = self._solve_r(i, j + 1)
            if test_down:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False
