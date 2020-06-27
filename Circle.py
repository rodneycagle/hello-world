#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:47:35 2020

@author: cagle_restricted
"""


import turtle
turtle.bye()
t   = turtle.getturtle()
t.color("green","blue")
t.begin_fill()
for x in range(2):
    t.circle(100)
    t.left(90)
t.end_fill()
t.begin_fill()
t.color("green","red")
for x in range(2):
    t.circle(100)
    t.left(90)
t.end_fill()
 