import sys
from itertools import permutations
input = sys.stdin.readline
n=int(input())
cost = list(map(int,input().split()))
sale = [[] for _ in range(n)]
for i in range(n):
    m=int(input())
    for _ in range(m):
        sale[i].append(list(map(int,input().split())))
a=permutations(range(0,n),n)
minimum = float('inf')
for i in a:
    cost_temp = cost[:]
    price = 0
    for j in i:
        price +=cost_temp[j]
        for k,s in sale[j]:
            cost_temp[k-1] = max(1,cost_temp[k-1]-s)
    minimum = min(minimum,price)
print(minimum)