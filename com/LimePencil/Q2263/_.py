import sys

def preorder(start,end,start_i,end_i):
    if start == end:
        print(postorder[start],end=" ")
        return
    root = postorder[end]
    print(root,end=" ")
    root_inorder = position_of_inorder[root]
    if start <=start+root_inorder-start_i-1:
        preorder(start,start+root_inorder-start_i-1,start_i,root_inorder-1)
    if start+root_inorder-start_i<=end-1:
        preorder(start+root_inorder-start_i,end-1,root_inorder+1,end_i)

n = int(sys.stdin.readline().rstrip("\n"))
sys.setrecursionlimit(10**9)
position_of_inorder = [0]*(n+1)
inorder = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
postorder = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
for i in range(n):
    position_of_inorder[inorder[i]] = i
preorder(0,n-1,0,n-1)
