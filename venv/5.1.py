matrix=[input().rstrip().split(':') for i in range(0,1)]


a=matrix[0][2]
b=a[2:4]

hh=int(matrix[0][0])
mm=int(matrix[0][1])
ss=int(a[0:2])

if (hh>=1 and hh<=12 ) and (mm >=00 and mm<=59) and (ss>=00 and ss<=59):
    if b=='AM':
        if hh==12:
            hh=0
            print('{}:{}:{}'.format('%02d' % hh, '%02d' % mm, '%02d' % ss))
        print('{}:{}:{}'.format('%02d'%hh,'%02d'%mm,'%02d'%ss))
    if b=='PM':
        hh=hh+12
        print('{}:{}:{}'.format('%02d'%hh,'%02d'%mm,'%02d'%ss))



