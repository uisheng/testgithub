# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d=pow(b,2)-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为任意实数'
            else:
                return '方程无解'
        else:
            x1=-c/b
            x2=x1
            return x1,x2 
    else:
        if d<0:
            return '方程无解'
        else:
            x1=math.sqrt(d/(4*a*a))-b/(2*a)
            x2=-math.sqrt(d/(4*a*a))-b/(2*a)
            return x1,x2