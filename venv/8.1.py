
n=int(input())

ar=list(map(int,input().rstrip().split()))



result=0

for i in range(0,n):

    if ar[i] in ar[0:i]:
        continue
    else:
        for j in range(i,n):
            if ar[i]==ar[j]:
                result+=1

    result=result-result%2

print(int(result/2))