"""
Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

Problem: Find the Runner-Up Score
"""

#Solution

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    first = runnerup = -100 #initialize minimum from the constrants
    first = max(arr)
    
    for i in range(n):
        if(arr[i]>runnerup and arr[i]<first):
            runnerup = arr[i]
        
    print(runnerup)
