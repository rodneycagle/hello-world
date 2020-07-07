#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:49:46 2020

@author: cagle_restricted
"""


name = input("What is your name?")
while name != " ":
    for x in range(100):
        print(name, end = " ")
    print()
    name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing")