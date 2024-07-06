
import math as m

print('\n--- Year / Month / Day __ Change ---\n')

days = int(input('Input number of days: '))
months = 0
years = 0

if days >= 365:
    years = m.floor(days/365)
    days = days - years*365

    if days >= 30:
        months = m.floor(days/30)
        days = days - months*30

if years == 0:
    if months == 0:
        if days == 0:
            print('{} year {} month {} day'.format(years, months, days))
        else:
            print('{} days'.format(days))
    else:
            print('{} year {} months {} days'.format(years, months, days))
else:
    print('{} years {} months {} days'.format(years, months, days))

