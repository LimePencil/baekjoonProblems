import sys
from collections import deque
from math import floor,log2


def DFS_recur(t):
    global graph
    if t>ITERATIONS:
        if largest == max_possible[ITERATIONS]:
            print(largest)
            exit()
        return
    for i in range(4):
        copy = [x[:] for x in graph]
        m =move(i)
        max_possible[t] = max(max_possible[t],m)
        if graph != copy and (max_possible[ITERATIONS] ==0 or m*power_of_2[ITERATIONS-(t)]>max_possible[ITERATIONS]):
            DFS_recur(t+1)
        graph = copy


# 0 up 1 left 2 down 3 right
def move(direction):
    maximum = 0
    if direction == 0:
        for j in range(n):
            idx = 0
            prev = 0
            for i in range(n):
                if graph[i][j] != 0:
                    if prev == graph[i][j]:
                        maximum = max(maximum,prev*2)
                        graph[idx-1][j] = prev*2
                        prev =0
                        graph[i][j] = 0
                    else:
                        prev = graph[i][j]
                        maximum = max(maximum,prev)
                        graph[i][j] = 0
                        graph[idx][j] = prev
                        idx+=1
                        
    elif direction == 1:
        for i in range(n):
            idx = 0
            prev = 0
            for j in range(n):
                if graph[i][j] != 0:
                    if prev == graph[i][j]:
                        maximum = max(maximum,prev*2)
                        graph[i][idx-1] = prev*2
                        prev =0
                        graph[i][j] = 0
                    else:
                        prev = graph[i][j]
                        maximum = max(maximum,prev)
                        graph[i][j] = 0
                        graph[i][idx] = prev
                        idx+=1
    elif direction == 2:
        for j in range(n):
            idx = n-1
            prev = 0
            for i in range(n-1,-1,-1):
                if graph[i][j] != 0:
                    if prev == graph[i][j]:
                        maximum = max(maximum,prev*2)
                        graph[idx+1][j] = prev*2
                        prev =0
                        graph[i][j] = 0
                    else:
                        prev = graph[i][j]
                        maximum = max(maximum,prev)
                        graph[i][j] = 0
                        graph[idx][j] = prev
                        idx-=1
    else:
        for i in range(n):
            idx = n-1
            prev = 0
            for j in range(n-1,-1,-1):
                if graph[i][j] != 0:
                    if prev == graph[i][j]:
                        maximum = max(maximum,prev*2)
                        graph[i][idx+1] = prev*2
                        prev =0
                        graph[i][j] = 0
                    else:
                        prev = graph[i][j]
                        maximum = max(maximum,prev)
                        graph[i][j] = 0
                        graph[i][idx] = prev
                        idx-=1
    return maximum
input = sys.stdin.readline
n = int(input().rstrip("\n"))
graph = []
ITERATIONS = 5
SUM = 0
ma = 0
for _ in range(n):
    arr = list(map(int,input().rstrip("\n").split(" ")))
    SUM += sum(arr)
    ma = max(ma,max(arr))
    graph.append(arr)
if n != 1:
    max_possible = [0]*(ITERATIONS+1)
    power_of_2 = [0]*(21)
    power_of_2[0] = 1
    largest = power_of_2[floor(log2(SUM))]
    for i in range(1,21):
        power_of_2[i] = 2*power_of_2[i-1]
    DFS_recur(1)
    print(max(max_possible))
else:
    print(graph[0][0])