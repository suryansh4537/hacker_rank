n=int(input())
mat=[[0 for x in range(n)] for y in range(n)]
for i in range(0,n):
        mat[i]=int(input().split())
print(mat)