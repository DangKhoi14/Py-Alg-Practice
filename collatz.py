countStart = 0
countEnd = 0
count = 0

n = int(input('Enter n: '))

while n > 1:

    if n % 2 == 0:
        n = int(n/2)
    else: n = int(3*n + 1)

    print('{}  '.format(n), end = '   ')

    if count == 10:
        print('\n')
        count = 0

    count = count + 1
