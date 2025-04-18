from window import Window
from maze import Maze
import sys

def main():
    NUM_COLS = 16    
    NUM_ROWS = 12
    # We'll leave margins between the screen border and the maze
    MARGIN = 50
    SCREEN_X = 800
    SCREEN_Y = 600
    CELL_SIZE_X = (SCREEN_X - 2 * MARGIN) / NUM_COLS
    CELL_SIZE_y = (SCREEN_Y - 2 * MARGIN) / NUM_ROWS

    sys.setrecursionlimit(10000)
    win = Window(SCREEN_X, SCREEN_Y)

    print("Creating Maze...")
    maze = Maze(MARGIN, MARGIN, NUM_ROWS, NUM_COLS, CELL_SIZE_X, CELL_SIZE_y, win, 7)
    print("Maze Created!")
    solved = maze.solve()
    if not solved:
        print("This maze cannot be solved! >:(")
    else:
        print("Maze solved! |:^)")
    win.wait_for_close()

if __name__ == "__main__":
    main()