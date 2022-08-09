import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
compatible = True
for i in range(len(arr1)):
    if arr1[i] == arr2[i]:
        compatible=False
        break
print("Y" if compatible else "N")