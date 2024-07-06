
def main():
    print('Min ___ Max Program checker\n')

    num = int(input('Input value to check: '))

    if num == 0:
        print('End Program !!!')
        return 

    min = num
    max = num

    while num != 0:
        if min >= num:
            min = num
        elif max <= num:
            max = num

        print('Min: ', min)
        print('Max: ', max)

        num = int(input('Input value to check(Input 0 to end program): '))

        if num == 0:
            print('End Program !!!')



main()