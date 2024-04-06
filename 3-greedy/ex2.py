list = [0,2,9,8,4]
result = 0
for item in list:
    if item <= 1 or result == 0 : result+=item
    else : result *= item

print(result)
