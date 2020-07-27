#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:49:02 2020

@author: cagle_restricted
"""


import turtle
turtle.bye()
t  = turtle.getturtle()
number = int(turtle.numinput("Number of sides or circles","How many sides or cirles in your shape?",6))
shape = turtle.textinput("Which shape do you want?","Enter 'p' for polygon or r' for rosette:")
for x in range(number):
    if shape == 'r':
        t.color("red", "blue")
        t.begin_fill()
        t.width(5)
       
        t.circle(100)
        
        t.left(360/number)
        
        t.end_fill()
    else:
        t.color("orange", "blue")
        t.width(10)
        t.forward(150)
        
        t.left(360/number)
        