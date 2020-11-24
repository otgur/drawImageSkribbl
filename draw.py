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

    def draw(self, x, y):
        if time.time() - 95 > self.time:
            return
        real_x = x_min + x/self.x_max * width
        real_y = y_min + y/self.y_max * height
        
        # TODO: use SendInput instead
        ctypes.windll.user32.SetCursorPos(int(real_x), int(real_y))
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0) # left up
        
        time.sleep(0.00001)
    
    def draw_colored(self, x, y, color: Color):
        raise NotImplementedError
    
    def setColor(self, color: Color):
        # click on color
        raise NotImplementedError


if __name__ == "__main__":
    d = Drawer(100, 100)
    
    for i in range(0, 100):
        d.draw(i, i)
        d.draw(i, 0)
        d.draw(0, i)
