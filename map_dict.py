#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:16:11 2023

@author: ernesto
"""

items = [
    {
     'product' : 'camisa',
     'price' : 100
     },
    {
     'product' : 'pantalon',
     'price' : 200
     },
    {
     'product' : 'pantalon 2',
     'price' : 150
     }
    ]

prices = list(map(lambda item : item['price'], items))

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes, items))

taxes = list(map(lambda new_items : new_items['taxes'], new_items))