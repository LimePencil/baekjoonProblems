import sys

n = int(sys.stdin.readline())

sizes = []
for i in range(n):
    sizes.append(list(map(int,("0 " + str(i) +" " +sys.stdin.readline()).strip('\n').split(" "))))
sizes.sort(reverse=True,key=lambda x: (x[2],x[3]))
for k,s in enumerate(sizes):
    rank = 1
    for i in range(k):
        prev = sizes[i]
        if(s[2] < prev[2]) and (s[3]< prev[3]):
            rank +=1
    s[0] = rank
ans =""
sizes.sort(key=lambda x: x[1])
for s in sizes:
    ans += str(s[0]) + " "
print(ans)