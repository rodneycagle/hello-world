#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:57:10 2020

@author: cagle_restricted
"""


rainy = input("How's the weather is it raining (y/n")
cold = input ("Is it cold outside? (y/n")
if (rainy == 'y' and cold == 'y'):
    print("You'd better wear a raincoat")
elif (rainy == 'y' and cold != 'y'):
    print("You'd better carry an umbrella")
elif (rainy != 'y' and cold == 'y'):
    print("Put on a jacket it's cold out")
elif (rainy != 'y' and cold != 'y'):
    print("Wear whatever you want, it's beautiful outside!")