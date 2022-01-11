import sys

def bellman_ford():
    distances = [inf]*(n+1)
    distances[1] = 0
    for i in range(n):
        for s,e,t in graph:
            if distances[e] > t+distances[s]:
                distances[e] = t+distances[s]
                if i == n-1:
                    return True
    return False

t= int(sys.stdin.readline().rstrip("\n"))
inf = 10**5
for _ in range(t):
    n,m,w = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    graph = []
    for i in range(m):
        s,e,time = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph.append((s,e,time))
        graph.append((e,s,time))
    for i in range(w):
        s,e,time = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        graph.append((s,e,-1*time))
    print("YES" if bellman_ford() else "NO")