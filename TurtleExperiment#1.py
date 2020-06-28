#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:08:32 2020

@author: phil
"""

import turtle
turtle.bye()
t   = turtle.getturtle()
t.color("green","blue")
t.begin_fill()
for x in range(4):
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.end_fill()
