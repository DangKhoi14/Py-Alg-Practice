
import math
print('---- TRÌNH GIẢI PHƯƠNG TRÌNH BẬC 2 ----')

while True:

    Flag = False
    a, b, c = 0, 0, 0

    try:
        a, b, c = map(float, input(
            'Nhập Hệ Số a, b, c Cách Nhau Bởi Khoảng Trống: ').split())

        Flag = True
    except:
        print('Lỗi đầu vào !!!')

    if Flag:
        if a == 0:
            if b == 0:
                if c == 0:
                    print('Phương Trình Vô Số Nghiệm')
                else:
                    print('Phương Trình Vô Nghiệm')
            else:
                print('Nghiệm Phương Trình Bậc 1 Vừa Nhập là x = ', c/b)
        else:
            delta = b*b - 4*a*c
            if delta > 0:
                print('Phương Trình Có Hai Nghiệm Phân Biệt')
                x1 = (- b + math.sqrt(delta))/2*a
                x2 = (- b - math.sqrt(delta))/2*a
                print('X1 = ', x1)
                print('X2 = ', x2)
            elif delta == 0:
                print('Phương Trình Có Nghiệm Kếp X1 = X2 = ', -b/(2*a))
            else:
                print('Phương Trình Vô Nghiệm')

    lists_1 = ['Y', 'YES']
    lists_2 = ['N', 'NO']
    lists = lists_1 + lists_2
    console = input('Tiếp Tục Giải Hay Không Yes/No --> ').upper()
    if console in lists_2:
        print('Kết thúc chương trình !!!')
        break
    elif console not in lists:
        print('Không hợp lệ, Chương Trình Sẽ Tự Tiếp Tục')
    else:
        print('Xác Nhận Lệnh --> Chương Trình Tiếp Tục')
