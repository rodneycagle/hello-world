#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:43:01 2020

@author: cagle_restricted
"""


import turtle
turtle.bye()
t   = turtle.getturtle()
t.color("green", "red")
t.width(5)
size = int(turtle.numinput("Triangle Size","What size triangle do you want?",300,100,560))

# intitialize turtle position
t.penup()

t.left(270)
t.forward(size/2)
t.left(270)
t.forward(size/2)
t.left(180)
t.pendown()

# triangle loop
t.begin_fill()
for k in range(3):
    t.forward(size)
    t.left(120)
t.end_fill()

