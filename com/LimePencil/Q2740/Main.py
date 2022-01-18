import sys

n, m = list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" ")))

arr1 = []
for i in range(n):
    arr1.append(list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" "))))

m, k = list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" ")))

arr2 = []
for i in range(m):
    arr2.append(list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" "))))


arr_ans = [[0 for _ in range(k)]for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            arr_ans[i][j] += arr1[i][l] * arr2[l][j]
for i in range(n):
    print(*arr_ans[i])