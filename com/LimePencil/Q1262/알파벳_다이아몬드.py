import sys

input = lambda: sys.stdin.readline().rstrip()
n,r1,c1,r2,c2 = list(map(int,input().split()))
for i in range(r1,r2+1):
    for j in range(c1,c2+1):
        rel_i=i%(2*n-1)
        rel_j=j%(2*n-1)
        dist=abs(n-rel_i-1)+abs(n-rel_j-1)
        if dist<n:
            print(chr(dist%26+97),end="")
        else:
            print(".",end="")
    print()