n=int(input())
m=[]

m.append(list(map(int,input().rstrip().split())))


n1=[0 for i in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        if m[0][i]==m[0][j]:
            n1[i]=n1[i]+1

maximum=max(n1)
s=2*10^5
for i in range(0,n):
    if n1[i]==maximum:
        n1[i]=m[0][i]
    else:
        n1[i]=s

print(min(n1))