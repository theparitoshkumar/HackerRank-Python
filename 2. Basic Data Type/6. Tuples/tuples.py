"""
Link: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

problem: tuples

"""


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    
    tp = tuple(integer_list)
    print(hash(tp))
