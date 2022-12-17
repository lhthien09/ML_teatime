# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:51:22 2022
Problem set: https://www.hackerrank.com/challenges/bday-gift/problem
@author: Ly Thien
"""

import math
import os
import random
import re
import sys

def solve(balls):
    return sum(balls)*0.5

if __name__=='__main__':
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    
    balls_count = int(input().strip())
    
    balls = []
    
    for _ in range(balls_count):
        balls_item = int(input().strip())
        balls.append(balls_item)
    
    result = solve(balls)
    
    fptr.write(str(result) + "\n")
    
    fptr.close()
