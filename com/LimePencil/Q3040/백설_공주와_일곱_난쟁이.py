import sys

input = sys.stdin.readline
arr = []
for _ in range(9):
    arr.append(int(input()))
s = sum(arr)-100
not_small = []
found = False
for i in range(9):
    for j in range(9):
        if i!= j and arr[i] + arr[j] == s:
            found = True
            not_small.append(i)
            not_small.append(j)
            break
    if found:
        break
for i in range(9):
    if i not in not_small:
        print(arr[i])