# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:14:21 2020

@author: School
"""


import turtle
turtle.bye()
t   = turtle.getturtle()
turtle.bgcolor("black")
colors = ["red", "yellow","blue","green","orange","purple","white","brown","gray","pink"]
family = []
name = turtle.textinput("My family","Enter a name, or just hit [ENTER]to end:")
while name != "":
    family.append(name)
    name = turtle.textinput("My family","Enter a name, or just hit [ENTER]to end:")

for x in range(100):
    t.pencolor(colors[x%8])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/len(family) + 2)