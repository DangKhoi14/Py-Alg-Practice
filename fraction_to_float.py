def fraction_input():
    fraction = input("Enter fraction: ")
    return fraction


def direction_check(fraction, locate):
    element = fraction[locate]

    if element.isdigit():
        return fraction[locate]

    elif element == "/":
        return "change_to_down"

    else:
        return "ERROR"


def main():
    fraction = fraction_input()
    up = ""
    down = ""
    result = [up, down]
    direction = 0

    for locate in range(len(fraction)):
        ret = direction_check(fraction, locate)

        if ret.isdigit():
            result[direction] += ret

        elif ret == "change_to_down":
            direction = 1

        else:
            print("ERROR")
            break

    up = float(result[0])
    down = float(result[1])

    print(up / down)


main()

# fraction = input('Enter fraction: ')

# fraction = fraction.split('/')
# try:
#     fraction = list(map(float,fraction))

#     print(fraction[0]/fraction[1])

# except:
#     print('Your input is not fraction !!')