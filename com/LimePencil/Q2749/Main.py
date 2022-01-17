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
                arr_ans[i][j] %= 1000000
    return arr_ans

sys.setrecursionlimit(10**5)
a = int(sys.stdin.readline().rstrip("\n"))
if a==0:
    print("0")
elif a == 1:
    print("1")
elif a== 2:
    print("1")
elif a == 3:
    print("2")
else:
    n = 2
    arr = [[1,1],[1,0]]
    new_arr = pow(arr,a-1)
    print(new_arr[0][0])