#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:57:12 2023

@author: ernesto
"""

import sys

print(sys.path)

import re

text = 'Mi número es 464 155 66 77, el código del país es +52 y tengo 33 años'

result = re.findall('[0-9]+', text)
result2 = re.findall('[a-z]', text)

import time

timesatamp = time.time()

local = time.localtime()
hora_local = time.asctime(local)

print(hora_local)

import collections

numbers = [1, 1, 2, 3, 4, 2, 3, 5, 66, 102, 110, 0, 4, 110]
counter = collections.Counter(numbers)
print(counter)