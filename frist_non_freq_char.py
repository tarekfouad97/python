def most_freq(str1:str):
    """
    Find the first non-repeating character in a string and its index.
    
    This function processes the input string to find the first character that appears
    exactly once, ignoring spaces and non-alphabetic characters. The search is case-insensitive.
    
    Args:
        str1 (str): The input string to analyze
        
    Returns:
        None: The function prints the first non-repeating character and its index,
              along with the frequency dictionary of all characters
        
    Raises:
        TypeError: If the input string is empty or None
    """
    if not str1:
        raise TypeError
    chars_list=[]
    chars_dict={}

    for char in str1:
        if char.lower() ==  " " or char.isalpha() != True:
            continue
        else:
            chars_list.append(char.lower())

            if char.lower() in chars_dict:
                chars_dict[char.lower()]+=1
            else:
                chars_dict[char.lower()]=1
    last_value=0
    last_key=""
    for key , value in chars_dict.items():
        if value == 1:
            last_key = key
            last_value =value
            break
    print(f"{last_key} index {chars_list.index(last_key)} ")
    print(f"{chars_dict}")
        
most_freq("Tarek Fouad Abdallah")