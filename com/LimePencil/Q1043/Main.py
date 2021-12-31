import sys

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
truth = list(sys.stdin.readline().rstrip("\n").split(" "))
if truth[0] == "0":
    print(m)
    for _ in range(m):
        sys.stdin.readline()
else:
    know = set(truth[1:])
    poss= [0]*m
    parties = []
    for i in range(m):
        l = list()
        parties.append(set(sys.stdin.readline().rstrip("\n").split(" ")[1:]))
        poss[i] = 1
    for _ in range(m):
        for i,k in enumerate(parties):
            if len(know.intersection(parties[i])) > 0:
                poss[i] = 0
                know = know.union(k)
    print(sum(poss))