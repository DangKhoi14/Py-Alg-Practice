import math as m

try:
    with open('Input2.inp', 'r') as bienfilenhap:
        dong1 = bienfilenhap.readline().strip()

        out = ''

        if dong1 == '1':
            dong2 = bienfilenhap.readline()
            a, b = map(float, dong2.split())

            if a == 0:
                if b == 0:
                    out = 'Phuong trinh co vo so nghiem'
                else:
                    out = 'Phuong trinh vo nghiem'
            else:
                out = 'Phuong trinh co nghiem: x = {}'.format(-b/a)

        elif dong1 == '2':
            dong2 = bienfilenhap.readline()
            a, b, c = map(float, dong2.split())

            if a == 0:
                if b == 0:
                    if c == 0:
                        out = 'Phuong trinh so vo nghiem'
                    else:
                        out = 'Phuong trinh vo nghiem' 
                else:
                    out = 'Phuong trinh co nghiem: x = {}'.format(-c/b)

            else:
                delta = b*b - 4*a*c

                if delta > 0:
                    x1 = float((-b+m.sqrt(delta))/2*a)
                    x2 = float((-b-m.sqrt(delta))/2*a)
                    out = 'Phuong trinh co 2 nghiem phan biet: \nx1 = {} \nx2 = {}'.format(x1, x2)
                elif delta == 0:
                    out = 'Phuong trinh co nghiem kep: x = {}'.format(-b/2*a)
                else:
                    out = 'Phuong trinh vo nghiem'

    with open('Output2.out', 'wb') as bienfilexuat:
        bienfilexuat.write(out.encode('utf8'))
except:
    print('ERROR !!!')
