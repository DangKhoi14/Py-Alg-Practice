
try:
    a, b, c = input('Nhập Phép Tính Đơn Giản Với Hai Giá Trị: ').split()

    a = float(a)
    c = float(c)

    if b == "+" or b =="cộng":
        print ('Kết quả: {} + {} = '.format(a, c), a + c)
    elif b == "-" or b == "trừ":
        print ('Kết quả: {} - {} = '.format(a, c), a - c)
    elif b == "*" or b == "x" or b == "X" or b == "." or b == "nhân":
        print ('Kết quả: {} x {} = '.format(a, c), a * c)
    elif b == "/" or b == ":" or b == "chia":
        print ('Kết quả: {} : {} = '.format(a, c), a / c)
    else:
        print ('Quá trình tính đã xảy ra lỗi hoặc phép tính không hợp lệ !!!')
except:
    print ('Dữ liệu đầu vào bị lỗi !!!')