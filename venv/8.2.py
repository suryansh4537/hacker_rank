npq=list(map(int,input().rstrip().split()))
ar=list(map(int,input().rstrip().split()))
r=[0 for z in range(0,npq[2])]
for i in range(0,npq[2]):
   r[i]=input()

temp=[]
def rotation():
    temp=ar[0:npq[0]-1]
    ar[0]=ar[npq[0]-1]
    ar[1:npq[0]]=temp

for x in range(0,npq[1]):
    rotation()

print(ar)