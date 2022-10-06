t = int(input())
for _ in range(t):
    e,n = map(int, input().split())
    ans = 0
    for i in range(n):
        x = int(input())
        if x > e:
              ans +=1
    print(ans)