import sys
url = sys.argv[1]

from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))

xmax, ymax = img.size

t = xmax/500

xmax = round(xmax/t)
ymax = round(ymax/t)

img = img.resize((xmax, ymax))

img = img.convert('1') # convert image to black and white

#img.show()

from draw import Drawer

d = Drawer(xmax, ymax)

for x in range(xmax):
    for y in range(ymax):
        #print(img.getpixel((x,y)))
        if(img.getpixel((x,y)) == 0):
            color = 0
            d.draw(x, y)
        else:
            color = 1
        