#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:33:39 2020

@author: cagle_restricted
"""


import turtle
turtle.bye()
t   = turtle.getturtle()
t.color("green", "red")
t.begin_fill()
t.penup()
t.left(180)
t.forward(150)
t.left(180)
t.pendown()
for x in range(3):
    t.forward(300)
    t.left(120)

t.end_fill()