from window import Window
from shapes import Point, Line, Cell

def main():
        
    win = Window(800, 600)
    #line = Line(Point(50,50), Point(400,400))
    #win.draw_line(line, "black")

    # # Cell with all walls but the left
    # cell = Cell(win)
    # cell.has_left_wall = False
    # cell.draw(50,100, 100,50)

    # # Cell with only bottom and top walls
    # cell = Cell(win)
    # cell.has_left_wall = False
    # cell.has_right_wall = False
    # cell.draw(100,50, 50, 0)

    # # Cell with all walls
    # cell = Cell(win)
    # cell.draw(0,150, 50,100)
    

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)


    win.wait_for_close()

if __name__ == "__main__":
    main()