'''
Mandelbrot set

A Mandelbrot set is a set of complex numbers.
When plotted these create a fractal  shape
Fractals are infinitely repeating patterns on different scales

We can define it using recursion

Mandelbrot is defined as a set of complex numbers: c
For which a infinite sequence of numbers is bounded z_0, z_1 ... z_n

So the magnitude of each complex number never exceeds this limit

z_0 = 0
z_n+1 = z_n ** 2 + c
'''
from operator import is_
import numpy as np
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt 


def z(n, c):
    if n == 0:
        return 0
    return z(n - 1,c) ** 2 + c

# c = 1 is not part of set as it grows without bound
print([z(x,1) for x in range(10)])

# We can do this with memorization

def sequence(c, z=0):
    while True:
        yield z 
        z = z ** 2 + c

def limit_seq(limit, c):
    for n, k in enumerate(sequence(c)):
        print(f"z({n}) = {k}")
        if n >= limit:
            break

'''
c = 1 is not in set as it grows to infinity
c = 0 is stable and stays at 0 
c = -1 is periodically stable and oscilates between 0 and -1
'''

#limit_seq(9, 1)
#limit_seq(9, 0)
#limit_seq(9, -1)
#limit_seq(9, -2)

'''
If we sample a series of values and plot them, cutting results which exceed our bounds we will get a fractal plot
'''

'''
Julia sets can also be generated using the same formula but with different starting conditions
There are infinitely many julia sets while only one mandelbrot set

For the julia set:
z_0 is a candidate value
c is a fixed constant
'''

def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)
    
def limit_fractal(limit, func):
    for n, k in enumerate(func):
        print(f"z({n}) = {k}")
        if n >= limit:
            break
#print(next(sequence(z=0, c=1)))
#limit_fractal(9, mandelbrot(-1))
#limit_fractal(9, julia(0, 0.25))

'''
Certain values of c produce connected julia sets. These are known as Fatou sets.
The can look like dust comprised of infinite number of pieces when plotted on the complex plane
'''

limit_fractal(40, mandelbrot(0.25)) # madelebrot as c=0.25 converges to 0.5 
limit_fractal(35, mandelbrot(0.26)) # slight change and our set diverges to infinity

'''
Plotting with numpy and matplotlib
'''

#Generate set of candidate values

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <=2

'''
Dirty Scatter plot

'''
def get_members(c, num_iterations):
    '''
    Filter our matrix to contain only stable complex numbers
    '''
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
members = get_members(c, num_iterations=20)
'''
plt.scatter(members.real, members.imag, color = "black", marker = ",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()

plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
'''
#Pillow rendering
from PIL import Image

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
image = Image.fromarray(np.invert(is_stable(c, num_iterations=20)))
image.show()
