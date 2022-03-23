import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
uni = ["Soongsil","Korea","Hanyang"]
if sum(arr)>=100:
    print("OK")
else:
    print(uni[arr.index(min(arr))])