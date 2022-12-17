# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:30:59 2022
Problem: https://www.hackerrank.com/challenges/extremely-dangerous-virus/problem
@author: Thien
"""

import math
import os
import random
import re
import sys

def solve(a, b, t):
    return pow(int((a+b)/2), t, 10**9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_mul_input = input().rstrip().split()
    
    a = int(first_mul_input[0])
    
    b = int(first_mul_input[1])
    
    t = int(first_mul_input[2])
    
    result = solve(a, b, t)
    
    fptr.write(str(result)+ '\n')
    
    fptr.close()