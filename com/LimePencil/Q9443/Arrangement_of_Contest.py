import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(set([input()[0] for _ in range(n)]))
arr.sort()
idx=0
while len(arr)>idx and ord(arr[idx][0])==65+idx:
    idx+=1
print(idx)