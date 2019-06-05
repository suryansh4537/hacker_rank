n=int(input())
matrix=[]
matrix.append(list(map(int,input().rstrip().split())))

total=0
max=0
min=0
temp=0
for i in range(0,n-1):
    if matrix[0][i]<matrix[0][i+1]:
      temp=matrix[0][i]
      matrix[0][i]=matrix[0][i+1]
      matrix[0][i+1]=temp

min=matrix[0][i+1]

for i in range(0,n-1):
    if matrix[0][i]>matrix[0][i+1]:
      temp=matrix[0][i]
      matrix[0][i]=matrix[0][i+1]
      matrix[0][i+1]=temp

max=matrix[0][i+1]

for i in range(0,n):
    total=total+matrix[0][i]

print(total-max,end="")
print(total-min)