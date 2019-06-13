
n=list(map(int,input().split()))

items=list(map(int,input().split()))
charged=int(input())

items[n[1]]=0
total=0
for i in range(0,n[0]):
    total=total+items[i]

actual=total/2
if actual==charged:
    print('Bon Appetit')
else:
    print(int(charged-actual))