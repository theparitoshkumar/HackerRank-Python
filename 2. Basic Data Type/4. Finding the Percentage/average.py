"""
Link:
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

Problem: Finding the percentage
"""


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
#Above code is written by the HackerRank to store dictionary elements.

avg = sum(student_marks[query_name])/3
print("%.2f"%avg)
