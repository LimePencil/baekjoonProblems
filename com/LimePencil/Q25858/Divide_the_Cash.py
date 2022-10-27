import sys

input = lambda: sys.stdin.readline().rstrip()
n,c = list(map(int,input().split()))
students = [int(input()) for _ in range(n)]
s=sum(students)
for solved in students:
    print(c*solved//s)
