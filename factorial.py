# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:15:34 2015

@author: aloverso
"""

def factorial(n):
    if n==1:
        return n
    return n * factorial(n-1)