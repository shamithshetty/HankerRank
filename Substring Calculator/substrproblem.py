# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:19:44 2020

@author: Shamith h shetty
"""

str="kincenvizh"
l=len(str)
print(((l*(l+1))/2)-(l-len(set((str)))))


# alternate method
'''
from itertools import combinations
str="kincenvizh"
length=len(str)
n=len(set([str[x:y] for x,y in combinations(range(length+1),r=2)]))
print(n)
'''