import sys

input = sys.stdin.readline

w = int(input())
area=0
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    area+=a*b
print(area//w)