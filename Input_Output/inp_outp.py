
try:
    with open('input.inp', 'r', encoding='utf8') as bien_a:
        Ten = bien_a.readline().rstrip('\n')
        TuoiHT = int(bien_a.readline()) + 20

    with open('output.outp', 'wb') as bien_b:
        Flag = '20 năm sau, tuổi của {} sẽ là {}'.format(Ten, TuoiHT)
        bien_b.write(Flag.encode('utf8'))

except FileNotFoundError:
    print('Không tìm thấy file')

except FileExistsError:
    print('Không tồn tại file')

except:
    print('Không hợp lệ')