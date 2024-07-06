
print ('Tính Tổng Dãy Số Nhập Bất Kì')

dayso = input('Nhập dãy các số cách nhau bởi khoảng trống: ')
danhsachso = dayso.split()
formated_danhsachso = map(int, danhsachso)

try:
    print ('Tổng Các Số Vừa Nhập Là: ', sum(formated_danhsachso))
except:
    print ('Lỗi người dùng nên không thể tính !!')