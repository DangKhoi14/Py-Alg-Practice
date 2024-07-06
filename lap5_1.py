
print('\nLap 5.1\n')

n = int(input('Input n ( array[n] ): '))
array = [n]
sum = 0
count = 0

i = 0
while i < n:
    array_i = int(input('Input array[{}]'.format(i)))
    array.append(array_i)
    sum = sum + array[i]
    i += 1

mean = round(sum / n,2)

i = 0
while i < n:
    if array[i] > mean:
        count += 1
    i += 1

print('Mean = ', mean)
if count > 1:
    print('{} numbers > mean'.format(count))
else:
    print('{} number > mean'.format(count))
