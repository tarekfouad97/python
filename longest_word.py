def longest_word(str1:str):
    """
    Find the longest word in a given string.
    
    This function processes the input string to find the word with the most
    alphabetic characters, ignoring any non-alphabetic characters in the word.
    
    Args:
        str1 (str): The input string to analyze
        
    Returns:
        None: The function prints the longest word found and its length
        
    Note:
        Non-alphabetic characters within words are removed before length comparison
    """
    list1 = str1.split()
    word = list1[0]
    length= len(list1[0])

    for words in list1[1:]:
        clean_word = "".join(char for char in words if char.isalpha())
            
        if len(clean_word) > length:
            length = len(clean_word)
            word = clean_word

    print(f" Longest word is {word} and length is {length}")


longest_word("hsh hhahha hhshdhshsdh ahshdhshdhsdhsahd ,,,,,,,,,,,,,,,,,,,,, as ahshh")
