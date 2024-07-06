
print ('Trình làm tròn chữ số')
Flag = False
try:
    a = float(input('Nhập số muốn làm tròn: '))
    b = int(input('Nhập giá trị làm tròn: '))
    Flag = True
    if Flag:
        print ('Xuất Kết Quả Bằng format: {0:.{1}f}'.format(a, b))

        print ('Xuất Kết Quả Bằng round: ', round(a, b))
except:
    print ('Nhập sai cmnr :))')
