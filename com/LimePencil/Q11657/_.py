import sys

def bellman_ford():
    distances = [inf]*(n+1)
    distances[1] = 0
    for i in range(n):
        for s,e,t in graph:
            if distances[s] != inf and distances[e] > t+distances[s]:
                distances[e] = t+distances[s]
                if i == n-1:
                    return True, distances
    return False, distances

inf = 10**8
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = []
for i in range(m):
    s,e,time = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph.append((s,e,time))
ans = bellman_ford()
if ans[0]:
    print("-1")
else:
    for a in range(2,n+1):
        dist = ans[1][a]
        if dist == inf:
            print("-1")
        else:
            print(dist)