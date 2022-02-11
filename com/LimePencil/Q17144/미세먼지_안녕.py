import sys

r,c,t = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
ans = 0
graph = []
purifier = []
for i in range(r):
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for j in range(c):
        if arr[j] >0:
            ans += arr[j]
        elif arr[j] == -1:
            purifier.append((i,j))
    graph.append(arr)
directions = [(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(t):
    newdust = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] >=5:
                count = 0
                for dx,dy in directions:
                    if  0<=x+dx<r and 0<=y+dy<c and graph[x+dx][y+dy] !=-1:
                        newdust[x+dx][y+dy] += graph[x][y]//5
                        count +=1        
                newdust[x][y] -= count*(graph[x][y]//5) 
    for x in range(r):
        for y in range(c):
            graph[x][y] += newdust[x][y] 
    px1,py1 = purifier[0]
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    now = 0
    ans -= graph[px1+directions[now][0]][py1+directions[now][1]]
    px1+=directions[now][0]
    py1+=directions[now][1]

    while not(px1 == purifier[0][0] and py1 == purifier[0][1]+1):
        dx,dy = directions[now]
        if 0<=px1+dx<=purifier[0][0] and 0<=py1+dy<c:
            graph[px1][py1] = graph[px1+dx][py1+dy]
            px1 = px1+dx
            py1 = py1+dy
        else:
            now=(now+1)%4
            continue
    graph[purifier[0][0]][purifier[0][1]+1] = 0

    px1,py1 = purifier[1]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    now = 0
    ans -= graph[px1+directions[now][0]][py1+directions[now][1]]
    px1+=directions[now][0]
    py1+=directions[now][1]
    while not(px1 == purifier[1][0] and py1 == purifier[1][1]+1):
        dx,dy = directions[now]
        if purifier[1][0]<=px1+dx<r and 0<=py1+dy<c:
            graph[px1][py1] = graph[px1+dx][py1+dy]
            px1 = px1+dx
            py1 = py1+dy
        else:
            now=(now+1)%4
            continue
    graph[purifier[1][0]][purifier[1][1]+1] = 0
print(ans)