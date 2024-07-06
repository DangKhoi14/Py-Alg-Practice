def main():
    print('--- Tax Calculator in Vietnam ---')

    while True:
        salary = float(input('Input Salary(VND): '))
        dependent_per = int(input('Input number of dependents: '))
        income_tax = salary - 11*10**6 - dependent_per*4.4*10**6


        if income_tax > 5*10**6:
            if income_tax > 10*10**6:
                if income_tax > 18*10**6:
                    if income_tax > 32*10**6:
                        if income_tax > 52*10**6:
                            if income_tax > 80*10**6:
                                level_7(salary, income_tax)
                                level, tax, money = level_7(salary, income_tax)
                            else:
                                level_6(salary, income_tax)
                                level, tax, money = level_6(salary, income_tax)
                        else:
                            level_5(salary, income_tax)
                            level, tax, money = level_5(salary, income_tax)
                    else:
                        level_4(salary, income_tax)
                        level, tax, money = level_4(salary, income_tax)
                else:
                    level_3(salary, income_tax)
                    level, tax, money = level_3(salary, income_tax)
            else:
                level_2(salary, income_tax)
                level, tax, money = level_2(salary, income_tax)
        else:
            level_1(salary, income_tax)
            level, tax, money = level_1(salary, income_tax)

        print('\n --- RESULT --- \n')
        print('Income taxes:', income_tax)
        print('level {}'.format(level))
        print('Salary that you inputed: ', salary)
        print('Number of dependents: ', dependent_per)
        print('Taxes: ', tax)
        print('Total amount you have after tax: ', money)

        console = input('Wanna again ?? "Yes" or "Y" to continue: ').upper()
        list_A = ['Y', 'YES']

        if console in list_A:
            print('The program continue !!')
        else:
            print('The program end !!')
            break

def level_1(salary, income_tax):
    level = 1
    tax = income_tax*5/100
    money = salary - tax

    return level, tax, money


def level_2(salary, income_tax):
    level = 2
    tax = 5*10**6*5/100 + (income_tax-5*10**6)*0.1
    money = salary - tax

    return level, tax, money


def level_3(salary, income_tax):
    level = 3
    tax = 5*10**6*0.05 + 5*10**6*0.1 + (income_tax-10*10**6)*0.15
    money = salary - tax

    return level, tax, money


def level_4(salary, income_tax):
    level = 4
    tax = 5*10**6*0.05 + 5*10**6*0.1 + 8*10**6*0.15 + (income_tax-18*10**6)*0.2
    money = salary - tax

    return level, tax, money


def level_5(salary, income_tax):
    level = 5
    tax = 5*10**6*0.05 + 5*10**6*0.1 + 8*10**6*0.15 + 14*10**6*0.2 + (income_tax-32*10**6)*0.25
    money = salary - tax

    return level, tax, money


def level_6(salary, income_tax):
    level = 6
    tax = 5*10**6*0.05 + 5*10**6*0.1 + 8*10**6*0.15 + 14*10**6*0.2 + 20*10**6*0.25 + (income_tax-52*10**6)*0.3
    money = salary - tax

    return level, tax, money


def level_7(salary, income_tax):
    level = 7
    tax = 5*10**6*0.05 + 5*10**6*0.1 + 8*10**6*0.15 + 14*10**6*0.2 + 20*10**6*0.25 + 28*10**6*0.3 + (income_tax-80*10**6)*0.35
    money = salary - tax

    return level, tax, money


main()
