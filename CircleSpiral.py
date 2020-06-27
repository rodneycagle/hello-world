#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:05:13 2020

@author: cagle_restricted
"""
import turtle
turtle.bye()
t   = turtle.getturtle()
turtle.bgcolor("orange")
t.color("green","blue")
t.begin_fill()
for x in range(4):    
 t.circle(100) 
 t.forward(200)
 t.left(90)
t.end_fill()

