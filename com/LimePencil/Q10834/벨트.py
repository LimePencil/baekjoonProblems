import sys

input = sys.stdin.readline
spin=0
rotation=1
for _ in range(int(input())):
    a,b,type = list(map(int,input().split()))
    rotation*=b
    rotation//=a
    if type==1:
        spin=1 if spin==0 else 0
print(spin,rotation)