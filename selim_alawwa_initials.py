# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 00:09:47 2018

@author: selem
"""

import turtle

def draw_selim_alawwa_initials(turtle):
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(60,60)
    turtle.goto(0,120)
    turtle.goto(60,180)
    turtle.penup()
    turtle.goto(90,0)
    turtle.pendown()
    turtle.goto(130,180)
    turtle.goto(170,0)
    turtle.penup()
    turtle.goto(105,75)
    turtle.pendown()
    turtle.goto(155,75)
    
selim = turtle.Turtle()
window = turtle.Screen()
window.setup( width = 1024, height = 768, startx = None, starty = None)
selim.speed(0)
draw_selim_alawwa_initials(turtle=selim)
window.exitonclick()