"""
Link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

Problem: Lists
"""


if __name__ == '__main__':
    N = int(input())
    commands = []
    arr = []
    
    # We run the loop till the N input to run the commands
    for i in range(N):
        commands = input().split()
        
        #Check each command one by one and perform the operations.
        if commands[0] == "append":
            arr.append(int(commands[1]))
        elif commands[0] == "print":
            print(arr)
        elif commands[0] == "sort":
            arr.sort()
        elif commands[0] == "pop":
            arr.pop()
        elif commands[0] == "reverse" :
            arr.reverse()
        elif commands[0] == "remove":
            arr.remove(int(commands[1]))
        elif commands[0] == "insert":
            arr.insert(int(commands[1]),int(commands[2]))
            