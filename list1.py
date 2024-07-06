
n = int(input())
test_list = []
for i in range(n):
    print('Input item {}: '.format(i+1), end='')
    item = input()
    test_list.append(item)

for i in range(n):
    print(test_list[i])