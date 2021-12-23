import sys

l,p= list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
ls = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
mul = l*p
ans = []
for i in ls:
    ans.append(i-mul)
print(*ans)