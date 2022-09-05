import sys

input = sys.stdin.readline
for i in range(int(input())):
    n,r1,c1,r2,c2=list(map(int,input().split()))
    s="YES" if (abs(r1-r2)==2 and abs(c1-c2)==1) or (abs(r1-r2)==1 and abs(c1-c2)==2) else "NO"
    print(f"Case {i+1}: {s}")