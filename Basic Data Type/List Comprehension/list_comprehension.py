"""
Link:
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

Problem: List Comprehension
"""

#Solution

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinate = []
    
    coordinate = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

                    
    print(coordinate)
