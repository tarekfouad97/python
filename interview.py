

def swap_count(a:str,b:str) -> int:
    total_count = 0
    for item in a:
        for item2 in b:
            if item == item2:
                index1= a.index(item)
                index2= b.index(item2)
                count = index2 - index1

                total_count = total_count+count
            



    return  total_count


if __name__ == "__main__" :


   