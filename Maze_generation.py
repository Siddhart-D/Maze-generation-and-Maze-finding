import random
import numpy as np
import turtle

graphsize, cellthickness, wallthickness = 30,15,5

def sumoflists(input):
    sum_l = 0
    for row in input:
        sum_l += sum(row)

def mazegeneration(x_axis,y_axis):
    walls = [[[1,1,1,1,1] for a in range(x_axis)] for b in range(y_axis)]
    x = 0
    y = 0