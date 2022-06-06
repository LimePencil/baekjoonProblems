import sys

input = sys.stdin.readline
for _ in range(int(input())):
    print("even" if int(input())%2==0 else "odd")