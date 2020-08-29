import random
from bezmerizing import Polyline
from flat import document, shape, rgb, rgba
from numpy.random import uniform, normal, choice
from scipy.stats import truncnorm

from scipy.stats import truncnorm
def t_normal(a, b, mu, sigma):
    tn = truncnorm((a-mu)/sigma, (b-mu)/sigma, loc=mu, scale=sigma)
    return tn.rvs(1)[0]

def draw():
    size = 200
    d = document(size, size, 'mm')
    page = d.addpage()
    fig = shape()
    page.place(fig.polygon( ((10, 10), (100, 10), (10, 100)) ) )   
    # uniform_fig = shape().nostroke().stroke(rgb(255, 0, 0)).width(1).nofill()
    # normal_fig = shape().nostroke().stroke(rgb(64, 220, 64)).width(1.5).nofill()
    # t_normal_fig = shape().nostroke().stroke(rgb(0, 128, 255)).width(2).nofill()
    # mu = 50 # center of normal distributions
    # sigma = 20 # standard deviation of normal distributions
    # sample_n = 400 # number of "samples" (i.e. circles to draw for each distribution)
    # for i in range(sample_n):
    #     c = uniform_fig.circle(uniform(100), uniform(100), 1)
    #     page.place(c)
    # for i in range(sample_n):
    #     c = normal_fig.circle(normal(mu, sigma), normal(mu, sigma), 1.5)
    #     page.place(c)
    # for i in range(sample_n):
    #     c = t_normal_fig.circle(t_normal(20, 80, mu, sigma), t_normal(20, 80, mu, sigma), 2)
    #     page.place(c)
    # d.pdf("test.pdf")
    return page.svg("test.svg")


draw()
