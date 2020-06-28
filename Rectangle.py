#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:44:03 2020

@author: phil
"""


import turtle
turtle.bye()
t   = turtle.getturtle()
turtle.bgcolor("black")
t.color("green", "red")
t.penup()
t.left(180)
t.forward(150)
t.left(180)
t.pendown()
t.begin_fill()
t.width(5)
for x in range(4):
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(180)
t.penup()   
t.forward(300)
t.pendown()

for x in range(4):
 t.left(180)
 t.forward(100)
 t.left(90)
 t.forward(100)
 t.left(180)
t.end_fill()