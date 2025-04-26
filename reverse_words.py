def reverse(str1:str):
    """
    Reverse the order of words in a string.
    
    This function takes a string and reverses the order of the words,
    maintaining the original order of characters within each word.
    
    Args:
        str1 (str): The input string to reverse
        
    Returns:
        None: The function prints the string with words in reverse order
    """
    reverse_list = 0
    reverse_list = str1.split()
    print(' '.join(reverse_list[::-1]))


reverse("I love you")