import sys

input = sys.stdin.readline
n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse=True)
print(sum([arr1[i]*arr2[i]for i in range(n)]))