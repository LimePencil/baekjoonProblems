import sys

input = sys.stdin.readline
n = int(input())
cnt=0
for _ in range(n):
    l,w,d,g=list(map(float,input().split()))
    if ((l<=56 and w<=45 and d<=25) or l+d+w<=125) and g<=7:
        print(1)
        cnt+=1
    else:
        print(0)
print(cnt)