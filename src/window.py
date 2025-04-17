from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        # Is window running ?
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry(f"{width}x{height}")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, color="black"):
        # x1, y1 = line.p1.x, line.p1.y
        # x2, y2 = line.p2.x, line.p2.y
        # return self.__canvas.create_line(x1, y1, x2, y2)
        line.draw(self.__canvas, color)
