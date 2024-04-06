list = "100011001011"

min = list[0]
max = list[-1]

if min == max:
    if min == "0": max="1"
    else: max = "0"

result = list.count(min+max)

print(result)
