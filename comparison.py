
name_a, heigh_a = input('Nhập Tên *khoảng trống* Chiều Cao Bạn Thứ Nhất: ').split()
name_b, heigh_b = input('Nhập Tên *khoảng trống* Chiều Cao Bạn Thứ Hai: ').split()

try:
    heigh_a = float(heigh_a)
    heigh_b = float(heigh_b)

    if heigh_a > heigh_b:
        diferrentvalue = heigh_a - heigh_b
        print ('Bạn {} cao hơn bạn {}'.format(name_a, name_b), diferrentvalue, 'cm')
    elif heigh_a == heigh_b:
        print ('Hai bạn có chiều cao bằng nhau')
    else:
        print ('Bạn {} cao hơn bạn {}'.format(name_b, name_a), heigh_b - heigh_a, 'cm')
except:
    print ('Tuổi Đầu Vào Không Hợp Lệ')