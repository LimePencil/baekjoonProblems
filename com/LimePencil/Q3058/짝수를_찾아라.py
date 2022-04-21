for _ in range(int(input())):
    ans=sorted(filter(lambda a: a%2==0,map(int,input().split())))
    print(sum(ans),ans[0])