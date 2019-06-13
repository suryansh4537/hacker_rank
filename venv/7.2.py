n=int(input())

if n>=1700 and n<=1918:
    if n%4==0:
        print(f'12:09:{n}')
    else:
        print(f'13:09:{n}')

if n>=1919 and n<=2700:
    if n%400==0 or (n%4==0 and not(n%100==0)):
        print(f'12:09:{n}')
    else:
        print(f'13:09:{n}')

