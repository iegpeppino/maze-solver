from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, pa, pb):
        self.pa = pa
        self.pb = pb
    
    def draw(self, canvas, color):
        canvas.create_line(
            self.pa.x,
            self.pa.y,
            self.pb.x,
            self.pb.y,
            fill=color,
            width=2
            )

