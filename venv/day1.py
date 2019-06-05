n=int(input())
mat=[[0 for x in range(n)] for y in range(n)]
for i in range(0,n):
    for j in range(0,n):
        mat[i][j]=int(input().split())