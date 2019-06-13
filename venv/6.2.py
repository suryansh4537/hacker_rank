n=int(input())
m=[]
r=[]
for i in range(0,n):
    m.append(list(map(int,input().rstrip().split())))
    r[i]=0

for x in range(0,n):
    if m[x][1]<m[x][2]:
        r[x]= m[x][1]+(m[x][2] - 1)

    elif m[x][1]==m[x][2]:
        
