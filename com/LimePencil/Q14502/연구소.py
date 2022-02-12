import sys
from collections import deque
from itertools import combinations


def BFS():
    ans = len(possible_combination)-3
    queue = deque()
    visited = [[False for _ in range(m)]for _ in range(n)]
    for v in viruses:
        queue.append(v)
        visited[v[0]][v[1]] = True
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            if 0<= x+dx <n and 0<=y+dy<m and possible[x+dx][y+dy] and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                ans -=1
                queue.append((x+dx,y+dy))
    return ans

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
graph = []
possible = [[False for _ in range(m)]for _ in range(n)]
possible_combination = []
viruses = []
for i in range(n):
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for j in range(m):
        if arr[j] ==0:
            possible[i][j] = True
            possible_combination.append((i,j))
        elif arr[j] == 2:
            viruses.append((i,j))
maximum = 0
for w1,w2,w3 in combinations(possible_combination,3):
    possible[w1[0]][w1[1]] = False
    possible[w2[0]][w2[1]] = False
    possible[w3[0]][w3[1]] = False
    maximum = max(BFS(),maximum)
    possible[w1[0]][w1[1]] = True
    possible[w2[0]][w2[1]] = True
    possible[w3[0]][w3[1]] = True
print(maximum)
