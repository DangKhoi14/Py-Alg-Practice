
try:
    a, b, c = map(float, input('Nhập Độ Dài 3 Cạnh: ').split())

    if a+b>c and a+c>b and b+c>a:
        print ('Độ dài ba cạnh vừa nhập có thể tạo thành tam giác')
    else:
        print ('Độ dài ba cạnh vừa nhập không thể tạo thành tam giác')
except:
    print ('Lỗi !!!')