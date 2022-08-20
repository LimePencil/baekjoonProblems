import sys

input = sys.stdin.readline
n,p,h = list(map(int,input().split()))
for _ in range(n):
    a=int(input())
    if a>h:
        h=a
        print(f"BBTV: Dollar reached {a} Oshloobs, A record!")
    if a<p:
        print(f"NTV: Dollar dropped by {p-a} Oshloobs")
    
    p=a