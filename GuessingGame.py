#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:21:30 2020

@author: cagle_restricted
"""

import random
the_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: ")) 
print(guess, "was the number! You win")