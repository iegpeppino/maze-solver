import unittest
import sys
import os

# Altering path in order to access the maze.py file  
SCRIPT_DIR = os.path.dirname(os.path.abspath('src/maze.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Test if the list containing cells has the right num of cols
        self.assertEqual(len(m1._cells), num_cols) 
        # Test if the column has the right amount of cells (rows)
        self.assertEqual(len(m1._cells[0]), num_rows)

if __name__ == "__main__":
    unittest.main()

