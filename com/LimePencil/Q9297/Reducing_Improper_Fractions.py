import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    n,d=list(map(int,input().split()))
    if n%d==0:
        print(f"Case {t}: {n//d}")
    elif n//d!=0:
        print(f"Case {t}: {n//d} {n%d}/{d}")
    else:
        print(f"Case {t}: {n%d}/{d}")