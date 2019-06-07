n=int(input())
matrix=[]
matrix.append(list(map(int,input().rstrip().split())))

max=0
for i in range(0,n-1):
    if matrix[0][i]>matrix[0][i+1]:
        temp=matrix[0][i]
        matrix[0][i]=matrix[0][i+1]
        matrix[0][i+1]=temp

max=matrix[0][i+1]

s=1
for i in range(0,n-1):
    if matrix[0][i]== max:
        s=s+1

print(s)