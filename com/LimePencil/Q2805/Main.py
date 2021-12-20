import sys

def get_tree(arr,cut):
    total = 0
    for i in arr:
        total += max(0,i-cut)
    return total
def binary_search(arr,low, high, target):
    if high >= low:
        mid = (low + high)//2
        trees_cut = get_tree(arr,mid)
        if trees_cut == target:
            return mid
        elif trees_cut < target:
            return binary_search(arr,low,mid-1,target)
        else:
            return binary_search(arr,mid+1,high,target)
    else:
        return low -1

n, m = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
trees = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
trees.sort()
print(binary_search(trees,0,trees[-1],m))
