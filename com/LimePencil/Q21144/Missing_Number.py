import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=input()
for i in range(1,n+1):
    c="".join(map(str,range(1,i+1)))
    if len(c)>len(s):
        print(n)
        break
    else:
        if s[:len(c)]!=c:
            print(i)
            break