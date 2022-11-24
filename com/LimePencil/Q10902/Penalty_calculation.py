import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
t_s=[]
s_s=[]
for _ in range(n):
    t,s=list(map(int,input().split()))
    t_s.append(t)
    s_s.append(s)
idx=s_s.index(max(s_s))
if s_s[idx]!=0:
    print(idx*20+t_s[idx])
else:
    print(0)