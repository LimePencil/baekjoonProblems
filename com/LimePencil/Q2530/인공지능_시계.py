import sys

h,m,s = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
added = int(sys.stdin.readline().rstrip("\n"))

s = (s+added)
m = (m+s//60)
s%=60
h = (h+m//60)%24
m%=60
print(str(h)+ " " + str(m)+" "+str(s))