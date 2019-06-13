f=[]
s=[]

f.append(list(map(int ,input().rstrip().split())))
s.append(list(map(int ,input().rstrip().split())))
result=0

for i in range(0,f[0][0]):

    for j in range(0,f[0][0]):
        if s[0][i]<s[0][j] and (s[0][i]+s[0][j])/f[0][1]==0:
            result = result+1

print(result)