for _ in range(int(input())):
    input()
    n=int(input())
    a=[int(input()) for _ in range(n)]
    print("YES" if sum(a)%n==0 else "NO")