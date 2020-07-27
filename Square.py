#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:27:35 2020

@author: cagle_restricted
"""


answer = input("do you want to make a square? y/n:")
if answer == 'y':
  print("Working...")

  import turtle
  turtle.bye()
  t   = turtle.getturtle()
  t.color("green", "red")

  t.width(5)
  size = int(turtle.numinput("Square Size","What size square do you want?",300,100,560))
  t.penup()
  t.left(270)
  t.forward(size/2)
  t.left(270)
  t.forward(size/2)
  t.left(180)
  t.pendown()
  t.begin_fill()
  for x in range(4):
    t.forward(size)
    t.left(90)
    
t.end_fill()
print("okay we're done")