import sys

def dfs(x,y,s,total):
    global maximum
    if total + max_val*(4-s) <= maximum:
        return
    if s>=4:
        maximum = max(total,maximum)
        return
    for ch in d:
        if 0<=ch[0]+x<n and 0<=ch[1]+y<m and not visited[ch[0]+x][ch[1]+y]:
            if s== 2:
                visited[ch[0]+x][ch[1]+y] = True
                dfs(x,y,s+1,total+arr[ch[0]+x][ch[1]+y])
                visited[ch[0]+x][ch[1]+y] = False
            visited[ch[0]+x][ch[1]+y] = True
            dfs(ch[0]+x,ch[1]+y,s+1,total+arr[ch[0]+x][ch[1]+y])
            visited[ch[0]+x][ch[1]+y] = False



d = [(-1,0),(1,0),(0,-1),(0,1)]
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
visited = [[False for _ in range(m)] for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
max_val = max(map(max, arr))
maximum = -1
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,arr[i][j])
        visited[i][j] = False
print(maximum)
        

