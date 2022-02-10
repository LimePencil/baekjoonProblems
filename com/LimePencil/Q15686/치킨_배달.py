import sys
from itertools import combinations
n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
house = []
chicken = []
for i in range(n):
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    for j in range(n):
        if arr[j] ==1:
            house.append((i,j))
        elif arr[j] ==2:
            chicken.append((i,j))
minimum = float('inf')
for comb in combinations(chicken,m):
    sum = 0
    for h in house:
        sum+=min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in comb])
        if sum >= minimum:
            break
    else:
        minimum = min(minimum,sum)
print(minimum)