import sys

input = sys.stdin.readline
n,d = list(map(int,input().split(" ")))
dist = [i for i in range(d+1)]
fast = []
for _ in range(n):
    s,e,le = list(map(int,input().split(" ")))
    if e<=d and s<=d:
        fast.append((s,e,le))
fast.sort()
for i in range(d+1):
    if i>0:
        dist[i] = min(dist[i],dist[i-1]+1)
    for s,e,length in fast:
        if s>i:
            break
        if i==s and dist[i]+length <dist[e]:
            dist[e] = dist[i]+length
print(dist[d])