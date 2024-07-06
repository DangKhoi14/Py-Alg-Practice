s = 0

for i in range(100):

    if i%2 == 0 or i == 1:
        continue 
    
    s = s + 1/i
    i+=1
result = 1/s

print(result)
    