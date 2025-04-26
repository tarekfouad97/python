def reverse(str1:str):
    """
    Reverse the order of words in a string and each word's characters.
    
    This function takes a string, reverses the order of the words,
    and also reverses the characters within each word.
    
    Args:
        str1 (str): The input string to reverse
        
    Returns:
        None: The function prints the reversed string with words and characters reversed
    """
    reverse_list = 0
    reverse_list = str1.split()
    for i in range (len(reverse_list)):
        
        reverse_list[i] = reverse_list[i][::-1]
        
    print(' '.join(reverse_list[::-1]))


reverse("I love you")