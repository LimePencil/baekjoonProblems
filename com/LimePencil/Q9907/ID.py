import sys

input = lambda: sys.stdin.readline().rstrip()
arr = list(map(int,list(input())))
w=[2,7,6,5,4,3,2]
a=0
for i in range(7):
    a+=arr[i]*w[i]
c=["J","A","B","C","D","E","F","G","H","I", "Z"]
print(c[a%11])