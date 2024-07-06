
print ('--- Trình Kiểm Tra Loại Tam Giác Qua Do065 Dài 3 Cạnh ---')

print ('\n')

while True:
    a, b, c =0, 0, 0
    Flag = False

    try:
        a, b, c = map(float, input('Nhập Độ Dài 3 Cạnh Cách Nhau Bởi Khoảng Trống: ').split())

        Flag = True
    except:
        print ('Lỗi Đầu Vào Không Hợp Lệ')

    if Flag:
        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                if a == b and a == c:
                    type = 'ĐỀU'
                elif a == b or b == c or a == c:
                    type = 'CÂN'
                elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
                    type = 'VUÔNG'
                elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
                    type = 'TÙ'
                else:
                    type = 'NHỌN'

                print ('{}, {}, {} là ba cạnh của một tam giác {}'.format(a, b, c, type))
            else:
                print ('{}, {}, {} không phải là độ dài ba cạnh của một tam giác nào cả !!')
        else:
            print ('Ba cạnh của tam giác không thể nhỏ hơn hoặc bằng 0 !!')

    console = input ('Tiếp Tục ? --> Y/N: ')
    if console == 'N' or console == 'n':
        print ('Chương trình kết thúc \n')
        break
    elif console == 'Y' or console == 'y':
        print ('Xác nhận lệnh --> Chương trình tiếp tục \n')
    else:
        print ('Không lợp lệ --> Chương trình mặc định tiếp tục \n')