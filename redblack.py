from random import random

wallet = 0
count = 0

running = True
col_list = ['NO', 'N']

ans = int(input('Enter 1 or 2: '))
bet = int(input('Bet: '))

while running:

    count = count + 1
    print(count)

    n = -10 + round(20*random())

    # ans = int(input('Enter 1 or 2: '))
    # bet = int(input('Bet: '))

    wallet = wallet - bet

    print('System number = {}'.format(n))

    if n % 2 == 0 and ans == 2:
        wallet = wallet + 2*bet
    elif n == 0:
        wallet = wallet + bet
    elif n % 2 != 0 and ans ==1:
        wallet = wallet + 2*bet
    else: bet = bet * 2

    print('Your wallet: {}\n'.format(wallet))

    if count == 20:
        col = input('Wanna quit ??')

        if col.upper() not in col_list:
            running = False
            
        count = 0
