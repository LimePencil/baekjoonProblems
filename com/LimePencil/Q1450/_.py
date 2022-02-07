import bisect
import sys

def dfs(s,e,i,l):
    if s > e:
        l.append(i)
        return
    dfs(s+1,e,i+arr[s],l)
    dfs(s+1,e,i,l)
def binary_search(start, end, key, arr):
    while start < end :
        mid = (start + end) // 2
        if arr[mid] <= key:
            start = mid + 1
        else :
            end = mid
    return end

n,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr1 = []
arr2 = []
ans = 0
dfs(0,n//2-1,0,arr1)
dfs(n//2,n-1,0,arr2)
arr2.sort()
for i in arr1:
    if c-i <0:
        continue
    ans+= bisect.bisect_right(arr2,c-i)
print(ans)