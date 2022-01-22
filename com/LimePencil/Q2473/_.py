import sys

n = int(sys.stdin.readline().rstrip("\n"))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
minimum = float('inf')
a1 = 0
a2 = 0
a3 = 0
for i in range(n-2):
    s = i+1
    e = n-1
    target = -1*arr[i]
    while s<e:
        se = arr[s]+arr[e]
        if abs(se+arr[i])<minimum:
            minimum = abs(se+arr[i])
            a1,a2,a3 = arr[i],arr[s],arr[e]
            if se+arr[i] == 0:
                break
        if se > target:
            e-=1
        else:
            s+=1
print(str(a1)+" " + str(a2)+ " " +str(a3))
