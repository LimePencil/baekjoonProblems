import sys

input = sys.stdin.readline
for _ in range(int(input())):
    y_score=0
    k_score=0
    for _ in range(9):
        y,k= list(map(int,input().split()))
        y_score+=y
        k_score+=k
    print("Yonsei" if y_score>k_score else "Korea" if k_score>y_score else "Draw")