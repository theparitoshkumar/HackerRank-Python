"""
Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

Problem: Write a Function
"""

#Solution

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True      
    else:
        leap = False                
            
    
    return leap

year = int(input())