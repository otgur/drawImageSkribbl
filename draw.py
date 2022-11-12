import ctypes
from colors import Color
import time

# canvas position and size
x_min = 473
width = 834
y_min = 222
height = 625

# ctypes, see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx
class Drawer:
    
    def __init__(self, x_max: int, y_max: int):
        self.x_max = float(x_max)
        self.y_max = float(y_max)

        self.time = time.time()
        self.color = Color.BLACK
        # click black and small pencil
    
    # scale point from rectangle (0, 0), (x_max, y_max) to rect. (x_min, y_min), (x_min + width, y_min + height) 
    def scale(self, x, y) -> (float, float):
        return (x_min + x/self.x_max * width, y_min + y/self.y_max * height)

    def draw(self, x, y):
        if time.time() - 95 > self.time:
            return
        real_x, real_y = self.scale(x, y)
        Drawer.click(real_x, real_y)
    
    def drawEdge(self, A: (int, int), B: (int, int)):
        high_x, high_y = self.scale(max(A[0], B[0]), max(A[1], B[1]))

        w = abs(A[0] - B[0])
        h = abs(A[1] - B[1])

        if w > h:
            # create constant for iteration
            low_y = self.scale(min(A[1], B[1]))
            
            for x in range(min(A[0], B[0]), int(high_x)):
                Drawer.click(x, low_y + x/high_x * high_y)
        else:
            # create constant for iteration
            low_x = self.scale(min(A[0], B[0]))

            for y in range(min(A[1], B[1]), int(high_y)):
                Drawer.click(low_x + y/high_y * high_x, y)

    def draw_colored(self, x, y, color: Color):
        raise NotImplementedError
    
    @staticmethod
    def click(x, y):
        # TODO: use SendInput instead
        ctypes.windll.user32.SetCursorPos(int(x), int(y))
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left up
        
        time.sleep(0.00001)

    def setColor(self, color: Color):
        # click on color
        raise NotImplementedError


if __name__ == "__main__":
    d = Drawer(100, 100)
    
    d.drawEdge((5, 5), (70, 100))
    d.drawEdge((20, 90), (50, 7))
