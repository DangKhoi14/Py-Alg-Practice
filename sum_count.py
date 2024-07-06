
while True:
    print('--- Chương Trình Liệt Kê Dãy Số Và Tính Tổng ---')
    
    a = int(input('Nhập a: '))
    b = int(input('Nhập b: '))

    s = 0
    for i in range(a, b+1):
        print(i)
        s = s + i
    print('Tổng',s)    

    console = input('Giải Tiếp ??   Y/N: ')
    if console == 'Y' or console == 'y':
         print('Xác Nhận Tiếp Tục !!')
    elif console == 'N' or console == 'n':
        print('Xác Nhận Lệnh END !!')
        break
    else:
        print('Không Xác Nhận --> Dừng')
        break