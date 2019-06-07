n=int(input())

data=[int(input()) for i in range(0,n)]
h=1
j=0

for i in data:
        h=1
        if i==0:
          h=1
        else:
            for x in range(0,i):
                if x%2==0:
                    h=h*2
                else:
                    h=h+1
        print(h)

