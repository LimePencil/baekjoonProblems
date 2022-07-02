import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    n,l=arr[0],arr[1:]
    avg=sum(l)/n
    greater=0
    for i in range(n):
        if l[i]>avg:
            greater+=1
    percent=greater*100/n
    percent+=0.00000001
    avg+=0.00000001
    print("{:.3f} {:.3f}%".format(avg,percent)) 