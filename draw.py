import pyautogui
from colors import Color

# canvas position and size
x_min = 473
width = 834
y_min = 222
height = 625

class Drawer:
    
    def __init__(self, x_max: int, y_max: int):
        self.x_max = float(x_max)
        self.y_max = float(y_max)
        
        # click black and small pencil

    def draw(self, x, y):
        real_x = x_min + x/self.x_max * width
        real_y = y_min + y/self.y_max * height
        pyautogui.click(real_x, real_y)
    
    def draw_colored(self, x, y, color: Color):
        raise NotImplementedError
    
    def setColor(self, color: Color):
        # click on color
        raise NotImplementedError


if __name__ == "__main__":
    d = Drawer(10, 10)
    
    for i in range(0, 10):
        d.draw(i, i)
    
