matrix=[]
matrix.append(list(map(int,input().rstrip().split())))
p=((matrix[0][2]-matrix[0][0])/(matrix[0][1]-matrix[0][3]))

r=list(range(0,10001))
if p in r:
    print('YES')

else:
    print('NO')
