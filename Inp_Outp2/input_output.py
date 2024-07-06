
try:
    with open('inp.inp', 'r', encoding='utf8') as bien_1:
        data = bien_1.readlines()
        str_joined = ' '.join(data).replace('\n', '')

        danhsachtu = str_joined.split()
        str_joined = ' '.join(danhsachtu)

    bien_2 = open('outp.outp', 'wb')
    Flag = 'File inp.inp có nội dung như sau: ' + str_joined
    bien_2.write(Flag.encode('utf8'))
except:
    print('Đã xảy ra lỗi !!!')