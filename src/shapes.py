from window import Window

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)
    
class Cell():
    def __init__(self,win):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def draw(self, x1, x2, y1, y2):
        if self._win is None:
            return
        # Overwrite class variables to avoid NoneType error
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        w = self._win

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if undo:
            color = "red"
        
        # Get the half of line's length of current cell
        crt_half_length = abs(self._x2 - self._x1) // 2
        # Calculate center coords of current cell
        crt_x_center = crt_half_length + self._x1
        crt_y_center = crt_half_length + self._y1

        # Get the half of line's length of the next cell
        to_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        # Calculate center coords of next cell
        to_x_center = to_half_length + to_cell._x1
        to_y_center = to_half_length + to_cell._y1

        line = Line(Point(crt_x_center, crt_y_center), Point(to_x_center, to_y_center))
        self._win.draw_line(line, color)
