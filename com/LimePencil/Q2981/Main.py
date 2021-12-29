import sys
import math
def GCD(a,b):
    if a< b:
        a,b =b,a
    while a !=0:
        temp = a
        a=b%a
        b=temp
    return b

n = int(sys.stdin.readline().rstrip("\n"))
m = []
for _ in range(n):
    m.append(int(sys.stdin.readline().rstrip("\n")))
m.sort()
ans=[]
gcd = m[1]-m[0]
for i in range(2,len(m)):
    gcd = GCD(m[i]-m[i-1],gcd)
for i in range(2,math.floor(math.sqrt(gcd)+1)):
    if gcd%i == 0:
        ans.append(i)
l = len(ans)
for i in range(l-1,-1,-1):
    if ans[i]**2!= gcd:
        ans.append(gcd//ans[i])
ans.append(gcd)
print(*ans)