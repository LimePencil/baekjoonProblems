import sys

def postorder(s,e):
    if s>e:
        return
    m = e+1
    for i in range(s+1,e+1):
        if tree[s]<tree[i]:
            m= i
            break
    postorder(s+1,m-1)
    postorder(m,e)
    print(tree[s])
sys.setrecursionlimit(10**6)
tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline().rstrip("\n")))
    except:
        break
postorder(0,len(tree)-1)