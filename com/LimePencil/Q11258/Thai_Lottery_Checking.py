import sys

input = sys.stdin.readline
prize = []
for _ in range(6):
    num,w=input().split()
    prize.append((num,int(w)))
while True:
    n=input().rstrip()
    if n=="-1":
        break
    ans=0
    if n==prize[0][0]:
        ans+=prize[0][1]
    
    if n[:3]==prize[1][0]:
        ans+=prize[1][1]

    if n[:3]==prize[2][0]:
        ans+=prize[2][1]
    
    if n[3:]==prize[3][0]:
        ans+=prize[3][1]
    
    if n[3:]==prize[4][0]:
        ans+=prize[4][1]
    
    if n[4:]==prize[5][0]:
        ans+=prize[5][1]
    print(ans)