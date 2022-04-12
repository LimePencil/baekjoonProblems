while True:
    n=int(input())
    if n==0:
        break
    print(min([input()for _ in range(n)],key=str.lower))