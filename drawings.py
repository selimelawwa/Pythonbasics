# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:35:43 2018

@author: selem
"""

import turtle

#Draw a circle of squares,
#the idea is to draw a square then roate 10 degrees and draw another when till you complete 360 degrees of a circle

def draw_square(turtle):
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)



def draw_circle_of_squares():
    window = turtle.Screen()
    window.bgcolor("red")
    window.setup( width = 600, height = 400, startx = None, starty = None)
    shape = turtle.Turtle()
    shape.speed(0)
    shape.fillcolor('yellow')
    shape.begin_fill()
    for i in range(1,37):
        draw_square(turtle=shape)
        shape.right(10)
    shape.end_fill()
    window.exitonclick()

draw_circle_of_squares()