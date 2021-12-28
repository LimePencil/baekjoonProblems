import sys



n = int(sys.stdin.readline().rstrip("\n"))
glasses = []
maximum = [0]*(n+1)
glasses.append(0)
for _ in range(n):
    glasses.append(int(sys.stdin.readline().rstrip("\n")))
maximum[0] = 0
maximum[1] = glasses[1]
if n>1:
    maximum[2] = glasses[1]+glasses[2]

for i in range(3,n+1):
    maximum[i] = max(glasses[i]+maximum[i-2],glasses[i]+glasses[i-1]+maximum[i-3])
    maximum[i] = max(maximum[i],maximum[i-1])
print(maximum[n])