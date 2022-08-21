import sys

input = sys.stdin.readline
s,v1,v2 = list(map(int,input().split()))
found=False
for i in range(int(s/v2)+1):
    if (s-v2*i)%v1==0:
        found=True
        print((s-v2*i)//v1,i)
        break
if not found:
    print("Impossible")