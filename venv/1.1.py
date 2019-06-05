n=int(input())
matrix = []
'''print("Enter the %s x %s matrix: "% (rows, columns))
'''
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))
s=0
t=0
u=n
for i in range(0,n):
    s=matrix[i][i]+s
    t = t + matrix[i][u-1]
    u=u-1

print(abs(s-t))