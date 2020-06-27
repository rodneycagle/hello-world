#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:38:25 2020

@author: cagle_restricted
"""
import turtle
turtle.bye()
t   = turtle.getturtle()
t.color("black", "red")
t.begin_fill()
for x in range(4):
 t.circle(100) 
 t.forward(200)
 t.left(90)
t.end_fill()

t.color("red", "black")

t.begin_fill()
for x in range(4):
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(180)
t.end_fill()

