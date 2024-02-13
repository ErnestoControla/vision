#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:04:07 2023

se desea tener una lista de numeros y procesarla para obtener 2 salidas.

en la primera se desean todos los numeros multiplicdos por 2 y en la segunda
los numeros de entrada multiplicados por 2 cuando dicha entrada sea diferente de 1

@author: ernesto
"""

numbers = [1, 1, -5, -6, 8]

mult_num = list(map(lambda x : x * 2, numbers))

mult = list(map(lambda x : x * 2 if(x != 1) else x, numbers))


