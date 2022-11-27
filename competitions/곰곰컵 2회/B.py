import sys

input = lambda: sys.stdin.readline().rstrip()

ans=0
s=set()
s.add("ChongChong")
for i in range(int(input())):
    a,b=input().split()
    if a in s:
        s.add(b)
    if b in s:
        s.add(a)
print(len(s))