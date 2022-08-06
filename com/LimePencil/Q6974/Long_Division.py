import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    m = int(input())
    print(n//m)
    print(n%m)
    print()