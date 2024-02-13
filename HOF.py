#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:54:07 2023

@author: ernesto

En este ejempo vamos a tener funciones de orden superior
"""

def increment(x):
    return x + 1

def Hig_ord_func(x, func):
    return x + func(x)

result = Hig_ord_func(3, increment)

# ahora realizamos el mismo ejercicio pero con lambda

increment_v2 = lambda x : x + 1

Hig_ord_func_v2 = lambda x, func : x + func(x) 

result_v2 = Hig_ord_func_v2(3, increment_v2)
