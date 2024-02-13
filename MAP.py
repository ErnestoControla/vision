#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:23:09 2023

@author: ernesto
"""

numbers = [1, 2, 3, 4]

numbers_2 = []

for i in numbers:
    numbers_2.append(i * 2)
    
numbers_3 = list(map(lambda x : x * 2 , numbers))

numbers_4 = [5, 6, 7]

result = list(map(lambda x, y : x + y, numbers, numbers_4))
    