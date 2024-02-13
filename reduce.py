#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 08:55:52 2023

@author: ernesto
"""

import functools

numbers = [1 , 2, 3, 4, 5]

result = functools.reduce(lambda counter, item : counter + item, numbers)