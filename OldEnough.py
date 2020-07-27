#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:27:32 2020

@author: cagle_restricted
"""


Driving_age = eval(input("What is the legal driving age where you live? "))
your_age = eval(input("How old are you?"))
if your_age >= Driving_age:
    print("you're old enough to drive")
if your_age < Driving_age:
     print("Sorry you can drive in", Driving_age - your_age, "years.")