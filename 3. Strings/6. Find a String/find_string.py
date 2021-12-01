"""
Link: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

Problem: Find A String
"""


def count_substring(string, sub_string):
    l = len(sub_string)
    count = 0
    for i in range(len(string)):
        if string[i:i+l] == sub_string:
            count += 1        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)