
def func_1(list1):
    count = 0
    lastcount = 0
    result =[]
    
    count = []
    for item in list1:
        count.append(len(item))
    x = min(count)

    

        
            










    if len(str1) > len(str2):
        count = len(str2)
    else :
        count = len(str1)

    for item in str1[:-count:-1]:
        for item2 in str2[:-count:-1]:
            if item == item2:
                result.append(item)
            else:
                continue
    print(str(result)[::-1])


func_1(["mohamed","ahmed","walemed"])