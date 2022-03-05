import sys

input = sys.stdin.readline
t= int(input())
for _ in range(t):
    n = float(input())
    print("${:.2f}".format(n*0.8))