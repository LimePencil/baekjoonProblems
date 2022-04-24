import sys

input = sys.stdin.readline
while True:
    a,b=input().split()
    if a=="0" and b=="0":
        break
    cnt=0
    len_a=len(a)
    len_b=len(b)
    a=[0]*max(1,len_b-len_a+1)+list(int(c) for c in a)
    b=[0]*max(1,len_a-len_b+1)+list(int(c) for c in b)
    for i in range(len(b)-1,0,-1):
        if a[i]+b[i]>9:
            cnt+=1
            a[i-1]+=1
    print(cnt)