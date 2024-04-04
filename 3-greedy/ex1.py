list = [2,3,1,2,2]
n = len(list);
list.sort()

count = 0
result = 0;


for item in list:
    count+=1
    if count == item:
        count = 0;
        result +=1
        
print(result)
