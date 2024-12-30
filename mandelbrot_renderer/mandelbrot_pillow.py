'''
from PIL import Image
from mandelbrotset import MandelbrotSet
import numpy as np
import warnings
warnings.filterwarnings("ignore")
'''    
from PIL import Image
from mandelbrotset import MandelbrotSet
from viewport import Viewport
from PIL import ImageEnhance

mb_set = MandelbrotSet(20, escape_radius=1000)
print(0.26 in mb_set)
print(0.26 not in mb_set)

w,h = 512, 512
scale = 0.0075
BLACK_AND_WHITE = "L"

image = Image.new(mode=BLACK_AND_WHITE, size=(w,h))
for y in range(h):
    for x in range(w):
        c = scale * complex(x - w/2, h/2 -y)
        instability = 1 - mb_set.stability(c, smooth=True)
        image.putpixel((x, y), int(instability * 255))
image.show()




mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)
image = Image.new(mode="L", size=(512, 512))
for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
    c = complex(pixel)
    instability = 1 - mandelbrot_set.stability(c, smooth=True)
    pixel.color = int(instability * 255)

enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(1.25).show()
