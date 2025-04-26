def most_freq(str1:str):
    """
    Find the most frequently occurring character in a string.
    
    This function processes the input string to find the character that appears
    most frequently, ignoring spaces and non-alphabetic characters. The search is case-insensitive.
    
    Args:
        str1 (str): The input string to analyze
        
    Returns:
        None: The function prints the most frequent character and its count
        
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
        if value > last_value:
            last_key = key
            last_value =value

    print(f"{last_key} is repeated for {last_value} times")
        
most_freq("Tarek Fouad Abdallah")