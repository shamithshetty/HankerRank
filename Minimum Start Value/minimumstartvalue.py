# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:40:09 2020

@author: Shamith h shetty
"""


def cal():
    a=[-5,4,-2,3,1-1,-6,-1,0,5]
    x=0
    sum=0
    while(1):
        x=x+1
        c=1
        for i in a:
            c=c+1
            sum=x+i
            if sum <=1:
                break
            if c==len(a):
                print(x)
                return
    

cal()    