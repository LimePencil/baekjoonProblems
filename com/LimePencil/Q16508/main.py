T=input()
N=int(input())
book_name=[]
book_price=[]
for _ in range(N):
    c,w = input().split()
    c=int(c)
    book_name.append(w)
    book_price.append(c)
m=float('inf')
for i in range(1,1<<N):
    b=str(bin(i)[2:]).zfill(N)
    alphabets=[0]*26
    alphabets_target=[0]*26
    price=0
    for k,c in enumerate(b):
        if c=="1":
            for d in book_name[k]:
                alphabets[ord(d)-ord('A')]+=1
            price+=book_price[k]
    for d in T:
        alphabets_target[ord(d)-ord('A')]+=1
    for i in range(26):
        if alphabets_target[i]>alphabets[i]:
            break
    else:
        m=min(m,price)
if m==float('inf'):
    print(-1)
else:
    print(m)