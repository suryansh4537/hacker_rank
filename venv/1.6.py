n=int(input())
Grades=[0 for i in range(0,n)]

mul=list(range(0,101,5))

for x in range(0,n):
    Grades[x]=int(input())
    if Grades[x]>=38:
        for i in mul:
            if abs(Grades[x]-i)<3 and i>Grades[x]:
                Grades[x]=i

print(Grades)


