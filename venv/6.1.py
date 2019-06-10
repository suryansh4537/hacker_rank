n=int(input())
chsq=[]
chsq.append(list(map(int,input().rstrip().split())))
dm=[]
dm.append(list(map(int,input().rstrip().split())))
ans=0
t=0
for i in range(0,n):
    t=0
    for j in range(0+i,dm[0][1]+i):
        if j<n:
         t=t+chsq[0][j]

    if t==dm[0][0]:
         ans=ans+1

print(ans)
