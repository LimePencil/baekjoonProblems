n=int(input())

print("int a;")
print("int *ptr = &a;")
if n>1:
    print("int **ptr2 = &ptr;")

if n>2:
    for i in range(3,n+1):
        print(("int {}ptr{} = &ptr{};").format("*"*i,i,i-1))