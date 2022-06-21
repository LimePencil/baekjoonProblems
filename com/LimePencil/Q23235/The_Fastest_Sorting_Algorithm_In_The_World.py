import sys

input = sys.stdin.readline
idx=1
while True:
    arr = list(map(int,input().split()))
    if arr==[0]:
        break
    print("Case {}: Sorting... done!".format(idx))
    idx+=1