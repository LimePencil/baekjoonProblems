import sys

def find_fib(n):
    def pow(n_arr,exp):
        if exp ==1:
            return arr
        
        new_arr = pow(n_arr,exp//2)
        new_arr = mul(new_arr,new_arr)

        if exp%2 ==1:
            new_arr = mul(new_arr,arr)
        return new_arr
    
    def mul(arr1,arr2):
        arr_ans = [[0 for _ in range(2)]for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    arr_ans[i][j] += arr1[i][k] * arr2[k][j]
                    arr_ans[i][j] %= 1000000007
        return arr_ans
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif n== 2:
        return 1
    elif n == 3:
        return 2
    else:
        arr = [[1,1],[1,0]]
        new_arr = pow(arr,n-1)
        return new_arr[0][0]

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

a=int(input())
print((find_fib((a if a%2==1 else a-1)+1)))