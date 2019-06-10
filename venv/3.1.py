n=int(input())
matrix=[]
matrix.append(list(map(int,input().rstrip().split())))

high=0
low=0
max=int(0)
min=matrix[0][0]
for x in range(0,n-1):

        if matrix[0][x]<matrix[0][x+1]:
            if matrix[0][x+1]>max:
                high=high+1
                max=matrix[0][x+1]

        elif matrix[0][x]>matrix[0][x+1] and matrix[0][x+1]<min:
            min=matrix[0][x+1]
            low=low+1



        else:
            high=high

print(high,low)