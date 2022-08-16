import sys

input = sys.stdin.readline

same=["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
diff=["Yakk","Doh","Seh","Ghar","Bang","Sheesh"]
for t in range(1,int(input())+1):
    a,b = sorted(list(map(int,input().split())),reverse=True)
    c=""
    d=""
    if a==b:
        c=same[a-1]
        print(f"Case {t}: {c}")
    else:
        c=diff[a-1]
        d=diff[b-1]
        if a==6 and b==5:
            d="Beesh"
        print(f"Case {t}: {c} {d}")