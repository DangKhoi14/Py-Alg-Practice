from turtle import color


colors = ['red', 'blue', 'orange', 'yellow', 'red']

# THÊM "green" vào cuối list
colors.append('green')
print(colors)

# Thêm phần tử VỊ TRÍ n
colors.insert(2, 'purple')
print(colors)

# Trả về vị trí "orange"
pos = colors.index('orange')
print(pos)

# ĐẾM có bao nhiêu "red"
total = colors.count('red')
print(total)

# XOÁ phần tử cuối list
colors.pop()
print(colors)

# In phần tử cuối và bị xoá
print(colors.pop())

# Sắp xếp các phần tử trong list
colors.sort()

print(colors)