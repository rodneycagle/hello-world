#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:03:25 2020

@author: cagle
"""

import turtle
turtle.bye()
scrn = turtle.Screen()
scrn.bgcolor("black")

t    = turtle.getturtle()

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green'] 
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 5 + 1)
    t.forward(x)
    t.left(20)
    
turtle.done()