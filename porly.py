import random
from bezmerizing import Polyline, Path
from flat import document, shape, rgb, rgba, command, path
import numpy as np
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

from scipy.stats import truncnorm

def flatten(t):
    from itertools import chain
    return list(chain(*t))

size = 200
black = rgb(0,0,0)
gray = rgb(200, 200, 200)
d = document(size, size, 'mm')
page = d.addpage()

# fig = shape().fill(gray).stroke(black)
# pa = fig.polygon((10, 10, 100, 10, 10, 100))
# pb = fig.polygon((20, 20, 110, 20, 20, 110))
# page.place(pb)

p = Path([
    command.moveto(10, 10),
    command.lineto(15, 25),
    # command.curveto(15, 30, 5, 30, 5, 25),
    command.closepath
])

fig = shape().stroke(rgb(40, 40, 40)).fill(gray) #.nofill()
pa = fig.path(p)
pb = fig.path(p.translate(3, 2))
pc = path.difference(p, p.translate(3, 2))
page.place(pa)
# page.place(fig.path(p.translate(3, 2)))
# page.place(fig.path(p.translate(20, 20).rotate(np.pi*0.125)))
# page.place(fig.path(p.translate(20, 20).rotate(np.pi*0.125).scale(1.5)))


#d.pdf("test2.pdf")
page.svg('test2.svg')
#page.image(ppi=92, kind="rgb").png("sketch_2020_08_29.png")