n=int(input())
matrix=[]
for i in range(0,1):
    matrix.append(list(map(int,input().rstrip().split())))

positive,negative,zero=0,0,0
for i in range(0,n):
    if matrix[0][i]>0:
        positive=positive+1

    if matrix[0][i]==0:
        zero=zero+1

    if int(matrix[0][i])<0:
        negative=negative+1

print('{0:.6f}'.format(positive/n))
print('{0:.6f}'.format(negative/n))
print('{0:.6f}'.format(zero/n))