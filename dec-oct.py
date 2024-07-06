
print ('Chuyển đổi thập phân sang bát phân')
IsParseDone = False
try:
    stp = int(input('Nhập số muốn chuyển đổi: '))
    IsParseDone = True
    if IsParseDone:
        print ('Số thập phân vừa nhập %d trong hệ bát phân là %o' %(stp,stp))
except:
    print ('Dữ liệu đầu vào không hợp lệ')
