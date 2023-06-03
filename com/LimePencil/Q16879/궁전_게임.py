# import sys

# input = lambda: sys.stdin.readline().rstrip()

# def mex(p):
#     for o in range(len(p)):
#         if o!=p[o]:
#             return o
#     return len(p)


# grundy_single=[[0]*70 for _ in range(70)]

# for i in range(1,70):
#     for j in range(i+1):
#         s=set()
#         # check diagonal
#         s.add(grundy_single[i-1][j-1]) 
#         # check horizontal
#         for k in range(1,i+1):
#             s.add(grundy_single[i-k][j])
#         # check vertical
#         for k in range(1,j+1):
#             s.add(grundy_single[i][j-k])
#         x=mex(sorted(s))
#         grundy_single[i][j]=x
#         grundy_single[j][i]=x
# for i in range(70):
#     for j in range(70):
#         if grundy_single[i][j]-(i+j)%3<10:
#             print("  "+str(grundy_single[i][j]-(i+j)%3)+" ",end="")
#         elif grundy_single[i][j]-(i+j)%3<100:
#             print(" "+str(grundy_single[i][j]-(i+j)%3)+" ",end="")
#         else:
#             print(str(grundy_single[i][j]-(i+j)%3)+" ",end="")
#     print()
import sys

input = lambda: sys.stdin.readline().rstrip()       

n = int(input())
c=0
for _ in range(n):
    x,y=map(int,input().split())
    c^=(x+y)%3+((x//3)^(y//3))*3
print("koosaga" if c else "cubelover")