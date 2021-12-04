"""
Link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

Probelm: Text Wrap

"""

import textwrap

def wrap(string, max_width):
    str = textwrap.wrap(string,max_width)
    str  = "\n".join(str)
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)