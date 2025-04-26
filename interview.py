def swap_count(a:str,b:str) -> int:
    """
    Calculate the total number of swaps needed to make two strings equal.
    
    This function counts the number of position differences between matching
    characters in two strings. It assumes that both strings contain the same
    characters, just in different positions.
    
    Args:
        a (str): First string to compare
        b (str): Second string to compare
        
    Returns:
        int: Total number of position differences between matching characters
    """
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


   