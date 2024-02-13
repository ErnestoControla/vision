#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:32:21 2023

@author: ernesto

para este ejemplo se tiene un arreglo de numeros y se desea filtrar.
en este caso solo se van a obtener en la salida los numeros pares.
"""

numbers = [1 , 2 , 3, 4, 5]

pair = list(filter(lambda x : x % 2 == 0, numbers))