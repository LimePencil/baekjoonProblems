# import sys

# input = lambda: sys.stdin.readline().rstrip()

# def mex(p):
#     for o in range(len(p)):
#         if o!=p[o]:
#             return o
#     return len(p)


# grundy_single=[[0]*10 for _ in range(10)]

# for i in range(1,10):
#     for j in range(i+1):
#         s=set()
#         if i-2>=0 and j-1>=0 or i-1>=0 and j-2>=0:
#             if i-2>=0 and j-1>=0:
#                 s.add(grundy_single[i-2][j-1])
#             if i-1>=0 and j-2>=0:
#                 s.add(grundy_single[i-1][j-2])
#             x=mex(sorted(s))
#             grundy_single[i][j]=x
#             grundy_single[j][i]=x
# for i in range(10):
#     for j in range(10):
#         if grundy_single[i][j]<10:
#             print("  "+str(grundy_single[i][j]) +" ",end="")
#         elif grundy_single[i][j]-(i+j)%3<100:
#             print(" "+str(grundy_single[i][j])+" ",end="")
#         else:
#             print(str(grundy_single[i][j])+" ",end="")
#     print()
import sys

input = lambda: sys.stdin.readline().rstrip()       

n = int(input())
c=0
for _ in range(n):
    x,y,t=input().split()
    x=int(x)
    y=int(y)
    if t=="P":
        c^=(x+y)%3+((x//3)^(y//3))*3
    elif t=="N":
        if min(x,y)%3==1:
            if abs(x-y)>0:
                c^=1
        elif min(x,y)%3==2:
            if abs(x-y)>1:
                c^=2
            else:
                c^=1   
    elif t=="K":
        if min(x,y)%2==0:
            c^=abs(x-y)%2
        else:
            c^=abs(x-y)%2+2 
    elif t=="B":
        c^=min(x,y)
    else:
        c^=x^y
print("koosaga" if c else "cubelover")