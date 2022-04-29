import sys

input = sys.stdin.readline

n = int(input())
people_inside= int(input())
m=people_inside
for _ in range(n):
    come,out = list(map(int,input().split()))
    people_inside+=come-out
    if people_inside<0:
        print(0)
        sys.exit()
    m=max(m,people_inside)
print(m)