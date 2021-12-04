"""
Link: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

Problem: String Formatting
"""

def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:])
    
    for i in range(1,number+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexa = str((hex(i)[2:]).upper())
        binary = str(bin(i)[2:])
        print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)