# Tried to solve with math but failed

# import math
# import sys

# n = int(sys.stdin.readline().rstrip("\n"))
# total = 0
# for a in range(0,n):
#     p = math.comb(n-1,a)
#     pos = (a)
#     neg = (n-1-a)
#     nums = pos - neg
#     c= 0
#     if nums >=0:
#         c = 9-nums
#     else:
#         c = 10+nums
#     b= p*c
#     total += b
# print(total%1000000000)
import sys

n = int(sys.stdin.readline().rstrip("\n"))

table = [[1 for i in range(10)] for j in range(n)]
table[0][0] = 0
for i in range(1,n):
    for j in range(10):
        if(j == 0):
            table[i][j] = table[i-1][j+1]
        elif(j == 9):
            table[i][j] = table[i-1][j-1]
        else:
            table[i][j] = table[i-1][j+1] + table[i-1][j-1]
print(sum(table[n-1])%1000000000)
