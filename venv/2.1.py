st=[]
st.append(list(map(int,input().rstrip().split())))
ab=[]
ab.append(list(map(int,input().rstrip().split())))
mn=[]
mn.append(list(map(int,input().rstrip().split())))
appple=[]
appple.append(list(map(int,input().rstrip().split())))
orange=[]
orange.append(list(map(int,input().rstrip().split())))

a1=0
a2=0
x=int(ab[0][0])

for i in appple:
    f=i
    if (f+x)>=st[0][0] and (f+x)<=st[0][0]:
        a1=a1+1

for i in orange:
    if i+ab[0][1]>=st[0][1] and i+ab[0][1]<=st[0][1]:
        a2=a2+1

print(a1)
print(a2)