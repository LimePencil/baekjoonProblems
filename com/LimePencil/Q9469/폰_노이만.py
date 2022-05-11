import sys

input = sys.stdin.readline
for _ in range(int(input())):
    t,d,a,b,c = list(map(float,input().split()))
    print(int(t),d/(a+b)*c)
