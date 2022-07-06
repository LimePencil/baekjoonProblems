import sys

input = sys.stdin.readline

for _ in range(int(input())):
    for _ in range(int(input())):
        a,b= list(map(int,input().split()))
        print(a+b,a*b)