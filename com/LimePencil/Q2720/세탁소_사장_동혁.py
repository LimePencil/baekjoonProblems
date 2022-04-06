for _ in range(int(input())):
    n=int(input())
    a=n//25
    n-=a*25
    b=n//10
    n-=b*10
    c=n//5
    n-=c*5
    d=n
    print(a,b,c,d)
