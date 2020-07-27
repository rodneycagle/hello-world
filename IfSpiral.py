#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:22:47 2020

@author: Phillip
"""

answer = input("Do you want to see a spiral? y/n:")
if answer == 'y':
    print ("Working...")
    import turtle
    turtle.bye()
    t   = turtle.getturtle()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("Okay we're done!")
