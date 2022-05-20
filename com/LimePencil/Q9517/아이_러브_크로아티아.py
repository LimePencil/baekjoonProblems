import sys

input = sys.stdin.readline

n = int(input())
time=0
for _ in range(int(input())):
    t,z=input().split()
    t=int(t)
    time+=t
    if time>=210:
        break
    if z=="T":
        n+=1
print(n%8 if n!=8 else 8)