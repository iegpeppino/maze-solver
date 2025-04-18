from shapes import Cell
import random
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            # Default win to None, otherwise tests fail
            win= None,
            seed= None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self.seed = seed
        if seed is not None:
            random.seed(seed)

        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        """Create a matrix and fill it with cells according to num_cols and num_rows"""

        # Populating matrix with columns
        for i in range(self._num_cols):
            col = []
            # Populating columns with cells according to num_rows
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        # Actually drawing the cells to canvas
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j, color="black"):
        """Calculate cell position based on its column and row numbers i,j"""
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2, color)
        self._animate()

    def _animate(self):
        """Slows draw time so the maze creation looks like
        its being drawn"""
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.035)
    
    def _break_entrance_and_exit(self):
        """Creates an entrance cell at the upper left corner 
        and an exit at the cell in the bottom right corner"""
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        """Creates a path from start to exit by recursively
        visiting adjacent cells and breaking walls between them"""
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check if adjacent cells have been visited
            # First check if the adjacent index is not out of bounds
            # right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited: 
                to_visit.append((i, j+1))
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            
            # If nowhere to go, exit the loop
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            # Select a random adjacent cell to visit
            next_cell = random.choice(to_visit)

            # Break walls between current cell and cell to visit
            # right
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # down
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # left
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # up
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False 

            # Recursion to visit another cell
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        """Resets visited status for all cells in maze
        so they can be reused to solve the maze after"""
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False