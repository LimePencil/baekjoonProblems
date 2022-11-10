import sys

input = lambda: sys.stdin.readline().rstrip()
n,k,l = list(map(int,input().split()))
num=0
teams=[]
for _ in range(n):
    team=list(map(int,input().split()))
    if min(team)>=l and sum(team)>=k:
        num+=1
        teams+=team
print(num)
print(*teams)