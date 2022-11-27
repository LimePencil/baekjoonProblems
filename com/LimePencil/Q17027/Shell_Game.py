import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
ans_1=0
ans_2=0
ans_3=0

loc_1=1
loc_2=2
loc_3=3
for _ in range(n):
    a,b,g = list(map(int,input().split()))
    if loc_1==a:
        loc_1=b
    elif loc_1==b:
        loc_1=a
    if loc_2==a:
        loc_2=b
    elif loc_2==b:
        loc_2=a
    if loc_3==a:
        loc_3=b
    elif loc_3==b:
        loc_3=a
    if g==loc_1:
        ans_1+=1
    if g==loc_2:
        ans_2+=1
    if g==loc_3:
        ans_3+=1
print(max(ans_1,ans_2,ans_3))
