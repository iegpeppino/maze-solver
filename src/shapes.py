from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, color):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=color,
            width=2
            )
    
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

