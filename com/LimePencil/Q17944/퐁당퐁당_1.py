import sys

input = sys.stdin.readline
n,t = list(map(int,input().split()))
increase=True
hand=0
for i in range(1,t +1):
    if increase:
        hand+=1
    else:
        hand-=1
    if hand==2*n:
        increase=False
    if hand==1:
        increase=True
print(hand)