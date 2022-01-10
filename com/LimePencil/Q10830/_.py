import sys
from operator import mod

def pow(n_arr,exp):
    if exp ==1:
        return arr
    
    new_arr = pow(n_arr,exp//2)
    new_arr = mul(new_arr,new_arr)

    if exp%2 ==1:
        new_arr = mul(new_arr,arr)
    return new_arr
    

def mul(arr1,arr2):
    arr_ans = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr_ans[i][j] += arr1[i][k] * arr2[k][j]
                arr_ans[i][j] %= 1000
    return arr_ans


n,p = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = []
for _ in range(n):
    arr.append(list(map(lambda x: x%1000,map(int,sys.stdin.readline().rstrip("\n").split(" ")))))
new_arr = pow(arr,p)
for i in range(n):
    print(" ".join(map(str,new_arr[i])))



