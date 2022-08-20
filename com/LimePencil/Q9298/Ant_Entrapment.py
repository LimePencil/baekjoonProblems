import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    ans = 0
    min_x=float('inf')
    max_x=float('-inf')
    min_y=float('inf')
    max_y=float('-inf')
    for _ in range(int(input())):
        x,y=list(map(float,input().split()))
        min_x=min(min_x,x)
        max_x=max(max_x,x)
        min_y=min(min_y,y)
        max_y=max(max_y,y)
    print(f"Case {t}: Area {(max_x-min_x)*(max_y-min_y)}, Perimeter {2*((max_x-min_x)+(max_y-min_y))}")